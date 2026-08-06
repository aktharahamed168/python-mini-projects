import os
from PyPDF2 import PdfReader, PdfWriter

print("===== PDF Splitter =====")

reader = PdfReader("sample_1.pdf")

os.makedirs("output", exist_ok=True)

for page_num in range(len(reader.pages)):
    writer = PdfWriter()

    writer.add_page(reader.pages[page_num])

    output_file = f"output/page_{page_num + 1}.pdf"

    with open(output_file, "wb") as file:
        writer.write(file)

print(f"\nSuccessfully split {len(reader.pages)} pages.")
