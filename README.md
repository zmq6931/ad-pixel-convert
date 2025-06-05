# Pixel Converter Tool

A simple web app for converting images to a specified pixel size (e.g., 24x24) using Streamlit.

## Features

- Upload or drag-and-drop an image (PNG, JPG, JPEG)
- Select a target pixel size (24x24, 32x32, 48x48, 64x64)
- Instantly preview the converted image
- Download the resized image with a custom filename

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/zmq6931/ad-pixel-convert.git
   cd ad-pixel-convert
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Then open the provided local URL in your browser.

## How it works

1. Upload or drag-and-drop your image.
2. Select the desired pixel size from the dropdown.
3. The app will display both the original and the resized image.
4. Click the download button to save the converted image. The filename will be in the format: `originalname_widthxheight.png`.
