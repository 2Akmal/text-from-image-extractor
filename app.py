import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator

# Set the path to the Tesseract executable (if needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

st.title("Text-From-Image Extractor")

# Streamlit file uploader for image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image file
    image = Image.open(uploaded_file)

    # Extract text from the image
    text = pytesseract.image_to_string(image)

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
