#You must make and submit your own test file and txt file with this assignment.

fileName = open('62_Text.txt', 'r')
def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")


def longestLine(fileName):
    #Given a file return the longest line from within that file
    with open(fileName, 'r') as f:
        longest = max(f, key=len)
    return longest.strip('\n')

def toBinary(binaryFile):
    functionBinary = open(binaryFile,'r')
    bucket = []
    spot = 0
    everything = functionBinary.readline()
    while len(everything) >1:
        bucket.append(everything[0:8])
        spot +=1
        everything = everything[8:]
    return (bucket)