import re

wordsDict = {"file":[],"word":[],"wordCount":[]}
lettersDict = {}

def cleanupLine(line):
    """Unwanted characters are all characters except a-z, A-Z, 0-9 and ' and should be replaced with a space
        long-term -> long term
        It's amazing, isn't it? -> Is's amazaing  isn't it"""
# re.sub will clean unwanted characters in the string "line" using regex
# I would have used an if statement to only allow the correct chars but I was on a time crunch
    stripped_line = re.sub('[\[\]/{}$-:_="><?.,)()]+', '', line)
    return stripped_line


def countWords(stripped_line):
    """For a stripped line, this function counts the words and updates
        the globla variable wordsDict{}.
        Note, we convert upper case words to lower case words"""
    global wordsDict
    wordsDict = sum(1 for match in re.finditer(r"\bthe\b", stripped_line))
    return wordsDict


def countLetters(stripped_line):
    """For a stripped line, this function counts the letters and updates
        the globla variable lettersDict{}.
        Note, we convert upper case letters to lower case
        Note2, numbers and ' should be ignored"""
    global lettersDict
    lettersDict = stripped_line.count("t")
    return lettersDict


def readFiles(filename):
    handle = open(filename, 'r')
    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)

def results():
    return [0,0,0,0,0,0]




################################
handle = open("text2.txt", "r")
line = handle.read()
stripped_line = cleanupLine(line)
countWords(stripped_line)
countLetters(stripped_line)
#print(stripped_line)
print(wordsDict)
print(lettersDict)