import PyPDF2 as pdf 

def extract_text (filename):
    regulation = open(filename,'rb')

    regReader = pdf.PdfFileReader(regulation)

    pages_num = regReader.numPages
    page_text =""

    for page_num in range (0,pages_num):
        page=regReader.getPage(page_num)
        page_text=page_text + page.extractText()

    regulation.close()
    return page_text
