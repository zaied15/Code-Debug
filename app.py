import streamlit as st
from PIL import Image
from api_calling import codeDebug

# 1. Page Setup
st.set_page_config(page_title="Debug Your code with AI", layout="wide")
st.title("Debug Your code with AI")
st.caption("Squash bugs in seconds with the power of artificial intelligence.")

# 2. Sidebar For Inquiry
with st.sidebar:
    st.header("Settings")
    upload_image = st.file_uploader("Upload your error screenshot or code file", type=["jpg", "jpeg", "png"])
    analyze_btn = st.button("Analyze code")
    if upload_image:
        if analyze_btn:
            image = Image.open(upload_image)
            st.image(image=image, caption="Uploaded Screenshot")


with st.container():
    if analyze_btn:
        if upload_image:
            with st.spinner("AI is analyzing your code..."):
                result = codeDebug(image)
                st.success("Debuggin Completed")
                st.markdown(result)
        else:
            st.warning("Please upload your Screenshot")

            
