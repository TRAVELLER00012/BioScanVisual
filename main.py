import streamlit as st

st.set_page_config(layout="wide", page_title="BioScan", page_icon="🧬")
st.markdown("""
""", unsafe_allow_html=True)

pg = st.navigation({
    "BioScan": [
        st.Page("homepage.py", title="Home"),
        st.Page("inference_workspace.py",title="Inference Workspace"),
        st.Page("documentation.py",title="Research Paper")
    ]
},
    position="sidebar"
)


if __name__ == "__main__":
    pg.run()