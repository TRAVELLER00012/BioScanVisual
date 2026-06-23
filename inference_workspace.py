import streamlit as st
import pandas as pd
import math
from model import process

st.title("Inference Workspace")
st.divider()

st.markdown("""
Upload a blood smear image and allow BioScan to automatically detect and classify Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets using the final trained YOLO26x model.
""")

col1, col2 = st.columns(2,vertical_alignment="center",border=True,gap="medium")

with col1:
    st.image("./images/5.png",caption="Example Image, at 40x Zoom")
with col2:
    st.image("./images/15.png",caption="Example Output")


st.space("small")

files = st.file_uploader("Upload Image(s)",type="image/*",accept_multiple_files=True)

file_count = len(files)
MAX_COLUMN_SIZE = 3
row_count = math.ceil(file_count/MAX_COLUMN_SIZE)
i = 0
for row in range(row_count):
    columns = st.columns(MAX_COLUMN_SIZE,vertical_alignment="center",gap="medium",border=True)
    for col in columns:
        with col:
            if i < file_count and files[i] is not None:
                st.image(files[i],caption=f"{files[i].name}")
                i+=1


st.space("medium")

files_dir = st.file_uploader("Upload images",accept_multiple_files="directory",type="image/*")
files_dir_count = len(files_dir)
MAX_COLUMN_SIZE = 3
row_count = math.ceil(files_dir_count/MAX_COLUMN_SIZE)
j = 0
for row in range(row_count):
    columns = st.columns(MAX_COLUMN_SIZE,vertical_alignment="center",gap="medium",border=True)
    for col in columns:
        with col:
            if j < files_dir_count and files_dir[j] is not None:
                st.image(files_dir[j],caption=f"{files_dir[j].name}")
                j+=1

st.space("medium")

def run_inference(model = "26x"):
    st.session_state["results"] = process([*files_dir, *files],model)


st.button("Process Images",disabled=(file_count + files_dir_count) == 0,width="stretch",on_click=run_inference)
if file_count + files_dir_count == 0:
    st.warning("Upload blood smear samples to run the model.")

st.info("""By Default, we are using YOLO26x model, our best performing model for running detections.
To analyse other models live performance check out the 'Advance' section of this page""")

total_rbc, total_wbc, total_platelets = 0,0,0

if "results" in st.session_state:

    results = st.session_state["results"]

    for idx, result in enumerate(results):
        classes = result.boxes.cls.cpu().numpy()

        total_platelets += int((classes == 0).sum())
        total_rbc += int((classes == 1).sum())
        total_wbc += int((classes == 2).sum())



df = pd.DataFrame([total_rbc,total_wbc,total_platelets],index=["RBC","WBC","Plateltes"],columns=["Count"])

  
st.dataframe(df)
st.bar_chart(df,horizontal=True)

st.divider()

st.subheader("Advance")

st.space("small")

MODEL_OPTIONS = {
    "YOLOv8m": "Balanced YOLOv8 model",
    "YOLOv8l": "Highest Metric Score",
    "YOLOv8x": "Large YOLOv8 Architecture",
    "YOLO11m": "Best Balance of Accuracy and Stability",
    "YOLO11l": "Large YOLO11 Architecture",
    "YOLO11x": "Experimental Benchmark Outcome",
    "YOLO26m": "Medium YOLO26 Architecture",
    "YOLO26l": "Consistent Practical Performance",
    "YOLO26x": "Selected Final Model",
    "YOLO26x-2": "2 Batch Final Model"
}
m = st.menu_button("Model Options",options=MODEL_OPTIONS.keys(),width="stretch")

if m:
    st.button(f"Images will be processed using: {m}",width="stretch",on_click=lambda: run_inference(m[5:]),disabled=(file_count + files_dir_count) == 0)
    st.info(MODEL_OPTIONS[m])