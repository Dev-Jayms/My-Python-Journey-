# This module import the PyPDF2 module
import PyPDF2

# with open("Python Crash Course.pdf", "rb") as pdf_file:
#     pdfReader = PdfFileReader(pdf_file)
#     # Read the PDF content
#     text = pdfReader.getPage(100).extractText()
#     print(text)


# This code count the words in a PDF file.
def count_words_in_pdf(file_path):
    with open(file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    words = text.split()
    return len(words)

file_path = "Python Crash Course.pdf"
word_count = count_words_in_pdf(file_path)
print(f"The PDF file contains {word_count} words.")