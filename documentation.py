import streamlit as st

st.title("Research Paper")
st.badge("2026-June",color="green")
st.pdf("./doc/BioScan-cmc.pdf",height=600)

st.space("small")

with open("./doc/BioScan-cmc.pdf","rb") as file:
    pdf_file = file.read()
    st.download_button("Download Paper",data=pdf_file,file_name="BioScan.pdf",mime="application/pdf",width="stretch")