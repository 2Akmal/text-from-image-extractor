import streamlit as st
from PIL import Image
import requests
from googletrans import Translator
import base64
import tempfile  # Import tempfile for creating a temporary file

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

try:
    with open(logo_path, "rb") as logo_file:
        encoded_logo = base64.b64encode(logo_file.read()).decode()
except FileNotFoundError:
    st.error(f"Logo file not found at path: {logo_path}")
    encoded_logo = ""

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
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
        temp_path = temp_file.name
        image.save(temp_path)

    # Extract text using OCR.Space API
    result = ocr_space_file(temp_path)
    text = result.get('ParsedResults')[0].get('ParsedText') if result.get('ParsedResults') else ""

    # Display the image and the extracted text
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("Extracted Text:")
    st.write(text)

    # Translate text to Urdu
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ur').text

    # Display the translated text
    st.write("Translated Text (Urdu):")
    st.write(translated_text)
else:
    st.write("Please upload an image file.")
