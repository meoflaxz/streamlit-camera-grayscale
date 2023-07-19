import streamlit as st
from PIL import Image

# Start camera
with st.expander("Start Camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    # L is single channel aka luminance
    gray_img = img.convert("L")

    # Render grayscale image in webpage
    st.image(gray_img)