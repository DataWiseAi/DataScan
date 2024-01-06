from pytesseract import image_to_string
from PIL import Image
import streamlit as st
from streamlit.runtime.uploaded_file_manager import UploadedFile


st.set_page_config(
    page_title="Data Scan",
    page_icon="❄️",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("Data Scan")
st.subheader(body="Your one stop solution to extract data from image at scale")
images = st.file_uploader(
    label="Kindly upload your image files here",
)
logo = Image.open("../assets/logo.png")
st.sidebar.title(body=logo)


def process_image(images: UploadedFile) -> list:
    result = []
    for image in images:
        config = r"--psm 6 --oem 3"
        image = Image.open(fp=image)
        text = image_to_string(image=image, config=config)
        result.append(text)
    return result


if images:
    outputs = process_image(images=images)
    for output in outputs:
        st.write(output)
        st.divider()
