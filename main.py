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


def readFiles(filename, keyword, letter, letterUpper):
    handle = open(filename, 'r')
    stripped_line = cleanupLine(handle)
    countWords(stripped_line, keyword)
    countLetters(stripped_line, letter, letterUpper)
    return countWords, countLetters



def results():
    return [0,0,0,0,0,0]




#handle1 = open("text1.txt", "r")
#line1 = handle1.read()
#stripped_line1 = cleanupLine(line1)
#wordCount1=countWords(stripped_line1, "to")
#letterCount1=countLetters(stripped_line1, "e", "E")





#handle2 = open("text2.txt", "r")
#line2 = handle2.read()
#stripped_line2 = cleanupLine(line2)
#wordCount2=countWords(stripped_line2, "the")
#letterCount2=countLetters(stripped_line2, "t", "T")



#handle3 = open("text3.txt", "r")
#line3 = handle3.read()
#stripped_line3 = cleanupLine(line3)
#wordCount3=countWords(stripped_line3, "computer")
#letterCount3=countLetters(stripped_line3, "w", "W")
readFiles("text1.txt", "to", "e", "E")
readFiles("text2.txt", "the", "t", "T")
readFiles("text3.txt", "computer", "w", "W")

#wordsDict = {"to":[x], "the":[x], "computer":[x]}
#lettersDict = {"e":[y], "t":[y], "w":[y]}

print(lettersDict)
print(wordsDict)

