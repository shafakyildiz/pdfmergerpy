# Import the libraries needed

import PyPDF2
import sys

inputs = sys.argv[1:]

# Define a function to merge pdfs


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


# Call the function
pdf_combiner(inputs)