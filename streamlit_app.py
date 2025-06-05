import streamlit as st
from PIL import Image
import io
import os

col1, col2 = st.columns([1.2, 8])
with col1:
    st.image("logo.png", width=90)
with col2:
    st.title("Pixel Converter Tool")


st.write("""
1. Upload or drag and drop an image below.
2. Select the target pixel size (e.g., 24x24).
3. View and download the converted image.
""")

# Image upload
uploaded_file = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"], accept_multiple_files=False)

# Pixel size selection
size_options = ["24x24", "32x32", "48x48", "64x64"]
selected_size = st.selectbox("Select pixel size", size_options, index=0)
width, height = map(int, selected_size.split('x'))

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)
    imageContainer = st.container()
    imageContainer.image(image, caption="Original Image")

    # Convert pixel size
    converted_image = image.resize((width, height), Image.NEAREST)
    st.write(f"Converted to {width}x{height} pixels:")
    imageContainer = st.container()
    imageContainer.image(converted_image, caption=f"{width}x{height} Pixel Image")

    # Download button
    buf = io.BytesIO()
    converted_image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    # Get original file name (without extension)
    original_name = os.path.splitext(uploaded_file.name)[0]
    new_filename = f"{original_name}_{width}x{height}.png"
    st.download_button(
        label="Download converted image",
        data=byte_im,
        file_name=new_filename,
        mime="image/png"
    )
