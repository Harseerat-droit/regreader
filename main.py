import extraction as e
from nltk.tokenize import word_tokenize
from nltk.tokenize import regexp_tokenize
from nltk.corpus import stopwords

text_of_pages = e.extract_text('secReg2.pdf')

#tokens = word_tokenize(text_of_pages)

tokens = regexp_tokenize(text_of_pages,pattern='\w+|\$[\d\.]+|\S+')
punctuations = ['(',')',';',':','[',']',',','.']
keywords = [word for word in tokens if not word in punctuations]

print (keywords)