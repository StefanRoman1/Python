import re
import xml.etree.ElementTree as ET

def function1(text):
    words = re.findall("[A-Za-z]+", text)    
    return words

def function2(regex, text, length):
    words = re.findall(regex, text)
    return [word for word in words if len(word) == length]

def function3(regex_list, text):
    words = []
    for regex in regex_list:
        aux = re.findall(regex, text)
        words.extend(aux)
    return words

def function6(text):
    words = re.findall("[A-Za-z]+", text)
    for word in words:
        if word[0] in "aeiouAEIOU" and word[-1] in "aeiouAEIOU":
            word = re.sub("[aeiouAEIOU]", "*", word)
    return words

def function7(cnp):
    #check if the CNP is valid using regex
    regex = r"[1|2|5|6][1-9][1-9][0-1][0-9][0-3][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
    if re.match(regex, cnp):
        return True
    return False

#Write a function that recursively scrolls a directory and displays those files whose name matches a regular expression given as a parameter or contains a string that matches the same expression.
import os
import re

def function8(path, regex):
    for(root, dirs, files) in os.walk(path):
        for file in files:
            match = 0
            if re.search(regex, file):
                match += 1
            f = open(os.path.join(root, file), "r")
            for line in f:
                if re.search(regex, line):
                    match += 1
            f.close()
            if match != 0:
                if match == 1:
                    print(file)
                else:
                    print(">>", file)








#print(function1("Hello1World2hello world!Hello"))
#print(function2("[A-Za-z]+", "Ana1Are Multe/ Mere", 3))
#print(function3(["[A-Za-z]+", "[0-9]+",], "Ana12Are Multe/ Mere"))
#print(function6("Annnnna arrrrrrrre mere"))
#print(function7("5011215394431"))