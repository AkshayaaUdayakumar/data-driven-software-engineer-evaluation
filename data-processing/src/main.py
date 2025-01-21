import os
from src.extract import extract_text
from src.parse import parse_text
from src.output import save_to_json
from src.config import PDF_INPUT_FOLDER, OUTPUT_FOLDER

def process_pdfs(input_folder, output_folder, use_ocr=False):
    """
    Process all PDFs in the input folder and save structured data to the output folder.
    """
    print(f"Processing PDFs in: {input_folder}")
    os.makedirs(output_folder, exist_ok=True)

    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_folder, file)
            output_file = os.path.join(output_folder, f"{os.path.splitext(file)[0]}.json")
            print(f"Processing file: {pdf_path}")

            # Extract text using the selected method
            text = extract_text(pdf_path, use_ocr=use_ocr)
            if text:
                print(f"Text extracted from {pdf_path}")
                structured_data = parse_text(text)
                save_to_json(structured_data, output_file)
                print(f"Saved structured data to: {output_file}")
            else:
                print(f"Failed to extract text from {pdf_path}")

if __name__ == "__main__":
    print("Starting PDF processing...")
    process_pdfs(PDF_INPUT_FOLDER, OUTPUT_FOLDER, use_ocr=False)
    print("Finished PDF processing.")
