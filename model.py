from ultralytics import YOLO
from PIL import Image
import streamlit as st

MODEL_PATHS = {
    "26x": "./models/26x-200.pt",
    "26l": "./models/26l-200.pt",
    "26m": "./models/26m-200.pt",
    "11x": "./models/11x-200.pt",
    "11l": "./models/11l-200.pt",
    "11m": "./models/11m-200.pt",
    "8x": "./models/8x-200.pt",
    "8l": "./models/8l-200.pt",
    "8m": "./models/8m-200.pt",
    "26x-2": "./models/26x-big.pt"
}
@st.cache_resource
def get_model(model_name):
    path = MODEL_PATHS.get(model_name, MODEL_PATHS["26x"])
    return YOLO(path)


def process(files, model_name="26x"):
    images = [Image.open(file) for file in files]

    model = get_model(model_name)

    return model.predict(
        source=images,
        conf=0.15,
        imgsz=2048,
        verbose=False,
        max_det=10000
    )