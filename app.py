import streamlit as st
from PIL import Image

from ocr import extract_text


st.set_page_config(
    page_title="AI Text Insight Visualizer",
    layout="wide"
)

st.title("AI Text Insight Visualizer")

st.write(
    "Convert image text into words and visualize word-level attention "
    "using an attention mechanism."
)

st.divider()

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.subheader("Uploaded Image")

    st.image(
        image,
        width=500
    )

    st.subheader("Extracted Text")

    text = extract_text(image)

    if text.startswith("OCR Error:"):
        st.error(text)

    elif text:
        st.text_area(
            "OCR Result",
            text,
            height=150
        )

    else:
        st.warning(
            "No text could be detected in the image."
        )