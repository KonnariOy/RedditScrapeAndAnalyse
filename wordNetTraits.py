import csv
from nltk.corpus import wordnet

#personality
#Init
class wordNetTrait:
    def __init__(self, author):
        self.testwordfromcsv = ""
        self.testwordfromperslist = ""
        self.totalpersonalityvalue = 0
        self.allthewordsinfile = 0
        self.author_name = author
        print(author)

    def semanticTestFromFile(self, personality, file):
        with open("./data/" + personality + ".txt", 'r') as f:
            for linea in f:
                self.testwordfromperslist = wordnet.synsets(linea.rstrip())
                if len(self.testwordfromperslist) is not 0:
                    self.allthewordsinfile += 1
                    with open(file + ".txt", "r") as iamwordfile:
                        for lineb in iamwordfile:
                            self.testwordfromcsv = wordnet.synsets(lineb.rstrip())
                            if len(self.testwordfromcsv) is not 0:
                                result = min(wordnet.path_similarity(self.testwordfromperslist[0],self.testwordfromcsv[0]), wordnet.path_similarity(self.testwordfromcsv[0],self.testwordfromperslist[0]))
                                if result is not None:
                                    self.totalpersonalityvalue = self.totalpersonalityvalue + result                    
        print(personality)
        print(self.totalpersonalityvalue / self.allthewordsinfile)

    def semanticTestFromWebpage(self, personality):
        with open("./data/" + personality + ".txt", 'r') as f:
            for linea in f:
                self.testwordfromperslist = wordnet.synsets(linea.rstrip())
                if len(self.testwordfromperslist) is not 0:
                    self.allthewordsinfile += 1
                    with open("./data/tocsv" + self.author_name + ".txt", "r") as iamwordfile:
                        for lineb in iamwordfile:
                            self.testwordfromcsv = wordnet.synsets((lineb.rstrip()).decode('utf-8'))
                            if len(self.testwordfromcsv) is not 0:
                                result = min(wordnet.path_similarity(self.testwordfromperslist[0],self.testwordfromcsv[0]), wordnet.path_similarity(self.testwordfromcsv[0],self.testwordfromperslist[0]))
                                if result is not None:
                                    self.totalpersonalityvalue = self.totalpersonalityvalue + result                    
        print(personality)
        print(self.totalpersonalityvalue / self.allthewordsinfile)
x = wordNetTrait("CoffeeCoffeeCoffeee")
x.semanticTestFromWebpage("Agreeable")
x.semanticTestFromWebpage("Conscientious")
x.semanticTestFromWebpage("Extraverted")
x.semanticTestFromWebpage("Openness")
x.semanticTestFromWebpage("Stable")
#Done