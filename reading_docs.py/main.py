import PyPDF2
import re
import os
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize


class ReadDocs:
    # Constants
    directory = "documents/"
    # Detecting the supported extension types.
    def detect_type():
        for files in os.walk("documents/"):
            for file in files[-1]:
                if file.endswith(".pdf"):
                    return file
                elif file.endswith(".rtf"):
                    return file
                elif file.endswith(".docx" or ".doc"):
                    return file
                else:
                    filename, file_extension = os.path.splitext(file)
                    print("File format {} on file {} is not supported.".format(file_extension, filename))
    # Open/read pdf formated doc and write to text file
    def convert_pdf(file, dir):
        with open(dir+file, 'rb') as pdf:
            pdfReader = PyPDF2.PdfFileReader(pdf)
            for pages in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pages).extractText()
                print(pageObj)
                if os.path.isfile("converted_pdf.txt") == False:
                    with open("converted_pdf.txt", 'a') as new_f:
                        new_f.write(pageObj)
            pdf.close()

    # Open/read pdf formated doc and write to text file
    def convert_pdf(file, dir):
        with open(dir+file, 'rb') as pdf:
            pdfReader = PyPDF2.PdfFileReader(pdf)
            for pages in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pages).extractText()
                print(pageObj)
                if os.path.isfile("converted_pdf.txt") == False:
                    with open("converted_pdf.txt", 'a') as new_f:
                        new_f.write(pageObj)
            pdf.close()

    # Text/Data organization & storage
    def text_data(doc_input):
        print(sent_tokenize(doc_input))
        # Regex matching (Title, Dates, Emails, Decriptions)
        return sent_tokenize(doc_input)
        # Key:Value pairing these sections
    def org_file():
        word_bag = ["EDUCATION", "EXPERIENCE", "SKILLS", "REFERENCES"]
        sections = {}
        with open("converted_pdf.txt", 'r') as text:
            for num, line in enumerate(text, 1):
                for title in word_bag:
                    if title in line.upper():
                        print("title: {} num: {}".format(title,num))
                        print(re.compile("(*\n){2})title"))
            # Create dict with Key=title and Val=line number
            # Use Regex to clump sections together
            # NLTK the clumps to make sense out of it  https://superuser.com/questions/900411/how-to-capture-a-couple-of-lines-around-a-regex-match
        text.close()

    # Open and read a docx format
    """def open_docx(file, dir):
        with open(dir+file, 'r') as f:
            for line in f:
                print(line)"""
    # Open and read a  format
    """def open_rtf(file, dir):
        with open(dir+file, 'r') as f:
            for line in f:
                print(line)"""
    #detect_type()
    #convert_pdf(detect_type(),directory)
    org_file()
    #convert_pdf(detect_type(),directory)
