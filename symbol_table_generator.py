#Pegah Eizadkhah
#PYTHON SYMBOL TABLE PROJECT

#This Python program runs on a correct LC3 file given by the user and retrieves
#the labels (LC3 keywords) in the files along with their address and puts them in a
#symbol table displayed to the user. In addition the user can retrieve the
#address of a label from the symbol table by specifying the label. 

#This code is owned by Pegah Eizadkhah and is not meant for redistribution. 

import re
import sys

#first get rid of comments in text
file_name = raw_input("Please enter a file name: ")    
f = open(file_name , 'r')                 #open file 
g = open ('outfile.txt' , 'w')            #create dummy file

for line in f:                            #put contents of file in dummy file
    g.write(line)
f.close()
g.close()

g = open('outfile.txt' , 'r')             #open dummy file
fil = g.read()    
g.close()
w = open('out.txt', 'w')         
w.write(re.sub(r';.*', r'', fil))         #rewrite comments til the end of the line
w.close()                                 #with empty space

g = open ('out.txt', 'r')                 #comments are gone, reopen for reading

STRINGZ_ = '.STRINGZ'                                 
ORIG_ = '.ORIG'
x = 'x'
lineCount = 0

#make a list of words to ignore
toIgnore = ["AND", "ADD", "LEA", "PUTS", "JSR", "LD", "JSRR" , "NOT", "LDI" ,
            "LDR", "STI", "BR" , "JMP", "TRAP" , "JMP", "RTI" , "Br",
            "ST", "STR" , "BRz", "BRn" , "HALT", ".END", "GETC",
            "BRp", "BRnzp", "BRnz", "BRnp", "BRzp", "BRzn", "BRpz", "BRpn", "OUT"]

label = []            
instructions = []
data = list()

#this function gets the labels and line numbers and saves them in the tuple called "data"
def insert_data():
    for line in g:                                 
        if ORIG_ in line:                                       #if .ORIG is in line
            lineCount = int(line.split(x)[1]) -1                #lineCount = number next to it
        else:    
            if STRINGZ_ in line:                                #if .STRINGZ is in line
                string_len = 0
                stringz_ = line.split(STRINGZ_)[1].strip()      #read string    
                string_len = (len(stringz_)) - 2                #get string length
                
                        
            elem = line.split() if line.split() else ['']       #split line word for word
            if len(elem) > 1 and elem[0] not in toIgnore:       #if first word not in ignore list
                label.append(elem[0])                           #append to list of labels
                instructions.append(elem[1])
                lineCount += 1                                  #update line count
                if elem[1] == ".STRINGZ":                       #special case of .STRINGZ
                    lineCount = (lineCount + string_len)
                if elem[1] == ".BLKW":                          #special case for .BLKW
                    lineCount = (lineCount + int(elem[2]) - 1)
                data.append((elem[0], lineCount))               #store data in dictionary   
            elif elem[0] in toIgnore:                           #if word is in ignore list
                lineCount += 1                                  #update line count
                 
print()

#function to pretty print table 
def pretty_print():
    print()
    print('***THE SYMBOL TABLE***')
    longest = max([len(x[0]) for x in data])                    #adjusts according to longest word

    for j in data:
        a = j[0].ljust(longest)
        b = str(j[1])
        print (' '.join([a, b]))                                #prints results
       
insert_data()                                                  #function call on insert method
pretty_print()                                                 #function call on pretty-print
print() 

g.close() 
