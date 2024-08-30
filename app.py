import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from googletrans import Translator

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

# Streamlit app
st.title("Text-From-Image Extractor")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)

    # Save the uploaded file to a temporary location
    temp_path = "/tmp/uploaded_image.png"
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
