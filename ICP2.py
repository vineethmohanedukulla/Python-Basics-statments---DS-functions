# Question - 1 Approach - 1
"""each time we ask user to input if there are next heights to be entered if yes then enter the height or else we proceed for
calculation of conversion"""

inputList = []
nextHeight = 'Y'
while nextHeight == 'Y' or nextHeight == 'y':
    inputHeight = float(input("Enter the height you want to convert \n"))  # float method will typecast the input string to float
    inputList.append(inputHeight)   # appending the inputHeight to inputList
    nextHeight = input("Do you want to enter next height[Y/N] :")
newList = [x*2.54 for x in inputList]  # list comprehension way to represent a loop
print(newList)


# Question -1 Approach - 2
""" If User knows how many he has to convert and the list is large, then it becomes annoying to ask each time if he wants to enter next input
 Hence we take the number of entries first and then user types the inputs of that many"""
noOfHeights = int(input("Enter the number of heights you want to convert"))
n = 1
inputFlist = []
while noOfHeights != 0:
    inputFlist.append(float(input("Enter the height({0}) : ".format(n))))
    n = n + 1
    noOfHeights = noOfHeights - 1
newList = [x * 2.54 for x in inputFlist]  # list comprehensions
print(newList)

# Question : 2 -  Approach -1
first_name = input("enter the first name")
last_name = input("enter the last name")


def formfullname(firstname, lastname):
    return firstname + " " + lastname  # used string concatenation


fullname = formfullname(first_name, last_name)
print(fullname)

def string_alternativeapp1(fullnames):
    a = 0
    ss = ''
    for i in fullname:
        if a % 2 == 0:  # used percentile to check if the position is odd or even - appending only the even positions
            ss = ss + i
        a = a + 1
    return ss


outputapp1 = string_alternativeapp1(fullname)
print("Approach - 1 ", outputapp1)


# Question 2 : Approach -2
def string_alternativeapp2(fullnames):
    new_string = ""
    for x in range(0, len(fullnames), 2):
        new_string += fullnames[x]
    return new_string


outputapp2 = string_alternativeapp2(fullname)
print("Approach - 2 ", outputapp2)

# Question 3:
import string

input_file = open("input.txt", "r")
ddict = dict()

for eachline in input_file:
    eachline = eachline.strip()  # removes whitespaces in characters.
    eachline = eachline.lower()  # converting the entire line to lower case to avoid mismatches due to cases
    eachline = eachline.translate(eachline.maketrans("", "", string.punctuation)) # used to replace all punctuations(.,) etc with None
    words = eachline.split(" ")  # split used to break the line into words
    for eachword in words:
        if eachword in ddict:
            ddict[eachword] = ddict[eachword] + 1
        else:
            ddict[eachword] = 1
outputfile = open('output.txt', "a")
for key in list(ddict.keys()):
    line = "{0}: {1} \n".format(key, ddict[key])
    print(line)
    outputfile.write(line) # pushing the data into output file
outputfile.close() # to close the file stream