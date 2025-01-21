from PyPDF2 import PdfReader
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

def extract_text(pdf_path, use_ocr=False, lang="eng"):
    """
    Extracts text from a PDF file. Supports both text-based and scanned PDFs.
    """
    text = ""

    # Attempt text-based extraction with PyPDF2
    try:
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            text += page.extract_text()
        if text.strip():
            return text
    except Exception as e:
        print(f"PyPDF2 extraction failed for {pdf_path}: {e}")

    # Fallback to OCR if enabled
    if use_ocr:
        try:
            doc = fitz.open(pdf_path)
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                img = Image.open(io.BytesIO(pix.tobytes()))
                text += pytesseract.image_to_string(img, lang=lang)
        except Exception as e:
            print(f"OCR extraction failed for {pdf_path}: {e}")

    return text