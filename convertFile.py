import csv
import string
import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

#Init
class convertFile:
    def __init__(self, author_conv, file_type):
        self.unused = "." + file_type
        self.author_conv = author_conv

	## get attribute vectors by status
    def convertT(self):
        self.file_contenta = open("./data/tocsv" + self.author_conv + self.unused).read()
        tokens = word_tokenize(self.file_contenta.translate(None, string.punctuation))
        stopWords = set(stopwords.words('english'))
        wordsFiltered = []
        stemis = False
        ps = PorterStemmer()

        #Stopword and stem 
        for w in tokens:
            if w not in stopWords:
                if stemis is True:
                    wordsFiltered.append(ps.stem(w))
                else:
                    wordsFiltered.append(w)

        #Save
        with open("./data/tocsv" + self.author_conv + ".txt", 'w') as f:
            for item in wordsFiltered:
                if "http" not in item:
                    f.write("%s\n" % item)
x = convertFile("CoffeeCoffeeCoffeee", "csv")
x.convertT()
# Done