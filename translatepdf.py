Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
import io
from google.cloud import translate_v2 as translate
from google.cloud import vision
from google.cloud.vision import types
from PyPDF2 import PdfFileReader


# Set up the Google Cloud Translation API client
translate_client = translate.Client()

# Set up the Google Cloud Vision API client
vision_client = vision.ImageAnnotatorClient()

# Set the directory where the PDF files are stored
pdf_directory = "C:\Users\octav\Desktop\Bsc Electrical Eng. BME\6º Semester\Infocommunication\Hungarian Tests"

# Loop through each PDF file in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        # Read the PDF file
        pdf_file = open(os.path.join(pdf_directory, filename), 'rb')
        pdf_reader = PdfFileReader(pdf_file)
        page = pdf_reader.getPage(0)
        text = page.extractText()

        # Translate the text from Hungarian to English
        result = translate_client.translate(text, source_language="hu", target_language="en")

        # Print the translated text
        print(result['input'])
        print("==>")
        print(result['translatedText'])

        # Create an image from the PDF page
        image = types.Image(content=page.getContentStream().read())

        # Use the Google Cloud Vision API to detect the language of the original text
        response = vision_client.annotate_image({
            'image': image,
            'features': [{'type': vision.enums.Feature.Type.TEXT_DETECTION}]
        })
        detected_language = response.text_annotations[0].locale

        # Print the detected language and confidence score
        print(f"Detected language: {detected_language}")
        print(f"Confidence score: {response.text_annotations[0].confidence}")
