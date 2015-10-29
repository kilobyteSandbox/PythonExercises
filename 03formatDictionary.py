# 03formatDictionary.py

# Take a dictionary, and print it with formatting similar to a table of 
# contents or a menu


"""
# Older version of maxStringLength without max()
# Kept for nostalgia, to remind me of the youth and innocence
# of last week
def maxStringLength(dictionary):
    countK = 0
    countV = 0
    for k, v in dictionary.items():
        if len(str(k)) > countK:
            countK = len(str(k))
        if len(str(v)) > countV:
            countV = len(str(v))
    return countK, countV
"""


# Use to check the max string length of dictionary keys and values
def maxStringLength(dictionary):
    # Convert keys and values into string lists
    keyString = [str(i) for i in dictionary.keys()]
    valueString = [str(i) for i in dictionary.values()]
    # Return the length of the longest string for both keys and values
    return len(max(keyString, key=len)), len(max(valueString, key=len))


# Formats dictionary items like a menu or table of contents
# LeftPad and rightPad add extra padding to the left and right columns
def formatDictPrint(dictionary, title, leftPad = 0, rightPad = 0):
    # Used for header and line formatting
    topFill = "="
    lineFill = "."
    # Padding for left and right column
    leftColumn = maxStringLength(dictionary)[0] + leftPad 
    rightColumn = maxStringLength(dictionary)[1] + rightPad
    # Print title and title formatting
    print(title.center((leftColumn + rightColumn), topFill))
    # Print dictionary and format items
    for k, v in dictionary.items():
        print(str(k).ljust(leftColumn, lineFill) + \
            str(v).rjust(rightColumn))


# Demonstration of maxStringLength() and formatDictPrint()
sampleDictionary = {
    "First Item" : 44, "Second Item" : 12, "Third Item" : 101}

formatDictPrint(sampleDictionary, "Sample")
print(" ")
print(" ")
formatDictPrint(sampleDictionary, "Sample", 4, 2)