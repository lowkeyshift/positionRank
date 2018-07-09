import PyPDF2
import re
import os
import docx
from nltk import word_tokenize, pos_tag, ne_chunk, sent_tokenize


class ReadDocs:
    # Constants
    directory = "documents/"
    # Detecting the supported extension types
    # There are so many flaws here... But we can fix that later
    # Flaw 1. this function opens all files regardless of which converting function is run
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
                    # Spit out file name and extension that isn't supported
                    filename, file_extension = os.path.splitext(file)
                    print("File format {} on file {} is not supported.".format(file_extension, filename))
    # Open/read pdf formated doc and write to text file
    def convert_pdf(file, dir):
        with open(dir+file, 'rb') as pdf:
            pdfReader = PyPDF2.PdfFileReader(pdf)
            for pages in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(pages).extractText()
                print(pageObj)
                # If file doesn't exists, write new converted file
                if os.path.isfile("converted_pdf.txt") == False:
                    with open("converted_pdf.txt", 'a') as new_f:
                        new_f.write(pageObj)
            pdf.close()

    # Open/read docx formated doc and write to text file
    def convert_docx(file, dir):
        doc = docx.Document(dir+file)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        if os.path.isfile("converted_docx.txt") == False:
            with open("converted_docx.txt", 'a') as new_f:
                new_f.write('\n'.join(fullText))
            new_f.close()

    # Text/Data organization & storage # TBD: Theoretical NOT IN USE YET
    def text_data(doc_input):
        print(sent_tokenize(doc_input))
        # Regex matching (Title, Dates, Emails, Decriptions)
        return sent_tokenize(doc_input)
        # Key:Value pairing these sections

    # Spit out line numbers of the major sections of the resume file
    # This will later be used to do some basic math to separate resumes into sections based on the start & end of the titled sections
    # These chunks will be fed through the text_data() function to be sorted out and later added to database with a number ranking system
    def org_file(file):
        word_bag = ["EDUCATION", "EXPERIENCE", "SKILLS", "REFERENCES", "AWARDS"]
        sections = {}
        with open(file, 'r') as text:
            print("For file: {}".format(file))
            for num, line in enumerate(text, 1):
                for title in word_bag:
                    if title in line.upper():
                        print("title: {} num: {}".format(title,num))
            # Create dict with Key=title and Val=line number
            # Use Regex to clump sections together
            # NLTK the clumps to make sense out of it  https://superuser.com/questions/900411/how-to-capture-a-couple-of-lines-around-a-regex-match
        text.close()

    # Open and read a format
    # This will just work, will later feed into text_data()
    """def open_rtf(file, dir):
        with open(dir+file, 'r') as f:
            for line in f:
                print(line)"""
    #detect_type()
    #convert_pdf(detect_type(),directory)
    org_file("converted_docx.txt")
    convert_docx(detect_type(),directory)
