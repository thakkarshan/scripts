import os
import pypdf
from pypdf import PdfReader

folder_path = r"enter-path-to-folder"
search_term = "enter-search-term"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        pdf_file = open(os.path.join(folder_path, filename), "rb")
        pdf_reader = pypdf.PdfReader(pdf_file)
        print("Reading file...", filename)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            if search_term in text:
                print("---------------------")
                print(f"Found '{search_term}' in file {filename}, on page {page_num+1}")
                print("---------------------")
        pdf_file.close()

