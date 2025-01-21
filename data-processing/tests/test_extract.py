import os
from src.extract import extract_text

def test_extract_all_pdfs():
    pdf_directory = "/Users/akshayaaudayakumar/Desktop/pdf_processor/pdfs"

    # Iterate through all files in the directory
    for pdf_file in os.listdir(pdf_directory):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, pdf_file)
            print(f"Testing PDF: {pdf_path}")

            # Extract text
            text = extract_text(pdf_path)

            # Assertions
            assert text is not None, f"Extraction failed for {pdf_path}"
            assert len(text.strip()) > 0, f"Extracted text is empty for {pdf_path}"
            print(f"Extraction successful for {pdf_path}")
