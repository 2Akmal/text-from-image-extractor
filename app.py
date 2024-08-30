import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from googletrans import Translator
import base64  # Import base64 for encoding the logo

# Your OCR.Space API key
OCR_SPACE_API_KEY = 'K86735227088957'  # Replace with your actual API key

def ocr_space_file(filename, api_key=OCR_SPACE_API_KEY, language='eng'):
    """ OCR.Space API request function """
    url = 'https://api.ocr.space/parse/image'
    with open(filename, 'rb') as f:
        r = requests.post(url,
                          files={'file': f},
                          data={'apikey': api_key,
                                'language': language})
        return r.json()

# Load the local logo file and encode it to base64
logo_path = "logo/1678151870_1672293457.png"  # Adjust the path based on your directory structure

# Open the logo file and encode it
with open(logo_path, "rb") as logo_file:
    encoded_logo = base64.b64encode(logo_file.read()).decode()

# Display the logo in the header
st.markdown(
    f"""
    <style>
    .header {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px;
    }}
    .header img {{
        max-height: 100px;
    }}
    </style>
    <div class="header">
        <img src="data:image/png;base64,{encoded_logo}" alt="Logo">
    </div>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("Text-From-Image Extractor")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)

    # Save the uploaded file to a temporary location
    temp_path = "/tmp/uploaded_image.png"
    i
