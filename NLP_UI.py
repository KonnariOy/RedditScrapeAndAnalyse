import Tkinter
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import modelRun
import convertFile
import wordNetTraits
import fileProcess
import tweetProcess

fields =  'Username', 'Link website'

#For testing
personality = 'Openness'

#This will open the file
def uploadFile():
    filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("txt. files","*.txt"),("all files","*.*")))
#For testing
    print (filename)   
    x = convertFile(filename, "csv") # convert csv to txt
    x.convertT()
    wordNetTraits() # 
    
#This will make the forms, and labels of link
def make_form(top, fields):
    queries = []
    for field in fields:    
        row = Frame(top)
        label = Label(row, width=15, text=field, anchor='w')
        que = Entry(row)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        label.pack(side=LEFT)
        que.pack(side=RIGHT, expand=YES, fill=X)
        queries.append(que)        
    return queries

# Here will the code taking the link in will be placed
def run_code(q):
    user = q[0].get()
    link = q[1].get()
    
    fileProcess() # fetch and convert to csv
    convertFile() # convert csv to txt
    tweetProcess() # convert txt to csv
    modelRun() # personality test


#Printing the personality trait under the Label:"Personality trait analyzer"    
    result.configure(text = "Personality trait is: " + personality)  

#For testing    
    print(user, link)
    
#Main UI-loop    
if __name__ == '__main__':
    top = Tkinter.Tk()
    #Top label
    Tkinter.Label(top, text="Personality Trait Analyzer").pack()
    #Label for personality trait
    result = Tkinter.Label(top)
    result.pack()
    que = make_form(top, fields)
    top.bind('<Return>', (lambda event, q=que: run_code(q)))  
    #Buttons
    b1 = Tkinter.Button(top, text='Run',command=(lambda q=que: run_code(q)))
    b1.pack(side=Tkinter.LEFT, padx=5, pady=5)
    b2 = Tkinter.Button(top, text='Upload', command=uploadFile)    
    b2.pack(side=Tkinter.LEFT, padx=5, pady=5)    
    top.mainloop()