from pypdf import PdfWriter
from config import PDF_NAME as name_pdf

merger = PdfWriter()

pdf_s= []
n= int(input("How many files you want to merge? "))

for i in range(n):
    pdf_s.append(input(f"Enter the name of {i+1}th file:- "))

for pdf in pdf_s:
    merger.append(pdf)

merger.write(name_pdf)
merger.close()
