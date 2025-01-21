# PDF Processor

A Python program to extract structured data from PDFs and save it in JSON format.

## Problem Statement
Extract data from PDFs and store it in a structured format for further analysis. The solution should:
1. Handle text-based and scanned PDFs.
2. Be scalable to process a large number of files.


## Approach

Text-Based and Scanned PDFs

1. PyPDF2: Extracts text from text-based PDFs efficiently.
2. Tesseract OCR: Extracts text from scanned PDFs containing images.


### Key Advantages of This Approach
1. Simplicity: No complex batching or parallelization.
2. Scalability: Can process a large number of files sequentially without overloading memory.
3. Flexibility: Supports both text-based and scanned PDFs with minimal configuration.

## Limitations 
1. Slower due to image processing.
2. Requires Tesseract and language files.



## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd pdf_processor

## Commands to run 

1. python3 -m src.main - to get the output of extraction 
2. PYTHONPATH=$(pwd) pytest tests - to test the code