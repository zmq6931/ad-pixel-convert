import streamlit as st
from PIL import Image
import io
import os

st.title("🎈 Pixel Converter Tool")

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
    st.image(image, caption="Original Image", use_column_width=True)

    # Convert pixel size
    converted_image = image.resize((width, height), Image.NEAREST)
    st.write(f"Converted to {width}x{height} pixels:")
    st.image(converted_image, caption=f"{width}x{height} Pixel Image", use_column_width=False)

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
