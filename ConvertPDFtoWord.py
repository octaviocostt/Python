import os
import shutil
import glob
import PyPDF2
import docx

# Create a function to convert a single PDF file to Word format
def convert_pdf_to_word(input_file_path, output_folder_path):
    # Open the PDF file
    with open(input_file_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)
        
        # Create a new Word document object
        word_document = docx.Document()
        
        # Loop through each page of the PDF file
        for page_number in range(len(pdf_reader.pages)):
            # Get the current page
            page = pdf_reader.pages[page_number]
            
            # Extract the text from the page
            text = page.extract_text()
            
            # Add the text to the Word document
            word_document.add_paragraph(text)
        
        # Get the filename of the PDF file (without the extension)
        filename = os.path.splitext(os.path.basename(input_file_path))[0]
        
        # Save the Word document to a new file in the output folder
        output_file_path = os.path.join(output_folder_path, filename + '.docx')
        word_document.save(output_file_path)

# Set the input folder and output folder paths
input_folder_path = r'C:\Users\octav\Desktop\Bsc Electrical Eng. BME\6º Semester\Infocommunication\Hungarian Tests'
output_folder_path = r'C:\Users\octav\Desktop\Bsc Electrical Eng. BME\6º Semester\Infocommunication\Hungarian Tests\Word files'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Loop through each PDF file in the input folder
for input_file_path in glob.glob(os.path.join(input_folder_path, '*.pdf')):
    # Convert the PDF file to Word format
    convert_pdf_to_word(input_file_path, output_folder_path)

print("CODE DONE")
