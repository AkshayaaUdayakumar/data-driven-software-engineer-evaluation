# Input and output directories
PDF_INPUT_FOLDER = "./pdfs"
OUTPUT_FOLDER = "./output"

# Regex patterns for parsing
REGEX_PATTERNS = {
    "emails": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "dates": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
}

