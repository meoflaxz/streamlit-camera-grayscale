import streamlit as st
from PIL import Image


def parse(value):
    img = Image.open(value)
    gray_img = img.convert("L")
    st.image(gray_img)


def main():
    st.title("Image Processing App")
    uploaded_image = st.file_uploader("Upload Image")

    # Start camera
    with st.expander("Start Camera"):
        camera_image = st.camera_input("Camera")

    if camera_image:
        parse(camera_image)

    if uploaded_image:
        parse(uploaded_image)

if __name__ == "__main__":
    main()