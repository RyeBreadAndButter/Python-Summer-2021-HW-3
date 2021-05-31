import re


# re.sub will clean unwanted characters in the string "line" using regex
# I would have used an if statement to only allow the correct chars but I was on a time crunch
def cleanupLine(line):
    stripped_line = re.sub('[\[\]/{}$-:_="><?.,)()]+', '', line)
    return stripped_line

#This function will take a text file as a single string along with the desiered KEYWORD being counted
def countWords(stripped_line, keyword):
    global wordsDict
    wordsDict = sum(1 for match in re.finditer(keyword, stripped_line))
    return wordsDict

#This function will take a text file as a single string along with the desiered LETTER being counted
def countLetters(stripped_line, letter, letterUpper):
    global lettersDict
    lettersDict = stripped_line.count(letter) + stripped_line.count(letterUpper)
    return lettersDict


def readFiles(filename):
    handle = open(filename, 'r')
    for line in handle:
        stripped_line = cleanupLine(line)
        countWords(stripped_line)
        countLetters(stripped_line)

def results():
    return [0,0,0,0,0,0]




handle1 = open("text1.txt", "r")
line1 = handle1.read()
stripped_line1 = cleanupLine(line1)
wordCount1=countWords(stripped_line1, "to")
letterCount1=countLetters(stripped_line1, "e", "E")
#print(stripped_line)
print(wordsDict)
print(lettersDict)



################################
handle2 = open("text2.txt", "r")
line2 = handle2.read()
stripped_line2 = cleanupLine(line2)
wordCount2=countWords(stripped_line2, "the")
letterCount2=countLetters(stripped_line2, "t", "T")
#print(stripped_line)
print(wordsDict)
print(lettersDict)


handle3 = open("text3.txt", "r")
line3 = handle3.read()
stripped_line3 = cleanupLine(line3)
wordCount3=countWords(stripped_line3, "computer")
letterCount3=countLetters(stripped_line3, "w", "W")
#print(stripped_line)
print(wordsDict)
print(lettersDict)


wordsDict = {"to":[wordCount1], "the":[wordCount2], "computer":[wordCount3]}
lettersDict = {"e":[letterCount1], "t":[letterCount2], "w":[letterCount3]}

print(lettersDict)
print(wordsDict)

440
6209
119
1566
0
0

{'e': [6209], 't': [1566], 'w': [0]}
{'to': [415], 'the': [164], 'computer': [0]}