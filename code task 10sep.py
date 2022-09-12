# p1 palindrome using iterator(for loop) and generator mechanism.
str = 'kanma'
temp_str = ''
rev=str[::-1]
if rev==str:
    print("yes")
else:
    print("no")
def ispalindrome(string1):
    for i in range(int(len(string1)/2)):
        if string1[i]!=string1[len(string1)-i-1]:
            return"string is not palindrome"
    return"string is palindrome"
string1=input("Enter any string")
print(ispalindrome(string1))
# p3 Reverse string considering only alphabets. Symobls should not be reversed
def reverseString(text):
    index = -1
    for i in range(len(text) - 1, int(len(text) / 2), -1):
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text
string = "ab@#cd!ef"
print("Input string: ", string)
string = reverseString(list(string))
print("Output string: ", "".join(string))

# p4 findout elements duplicate count output in  dict format
listOfElems = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1
    dictOfElems = {key: value for key, value in dictOfElems.items() if value > 1}
    return dictOfElems
dictOfElems = getDuplicatesWithCount(listOfElems)
for key, value in dictOfElems.items():
        print(key , ' :: ', value)
## t1 = (1, 2, 3, "a", "c")
   # t2 = ("b", "d", 9, 8, 7)
   # Output: (10,10,10,"ab","cd")
t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)
l1 = []
l2 = []
for t in t1:
    if isinstance(t, int):
        for i in t2:
            if i not in l2 and isinstance(i, int):
                l2.append(i)
                l1.append((t + i))
                break
    else:
        for i in t2:
            if i not in l2 and isinstance(i, str):
                l2.append(i)
                l1.append((t + i))
                break
print(l1)

# p6 Write a Python program to remove leading zeros from an IP address.
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)
"""
# p8 l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]
   #output= [1,2,3,4,5,6,7,8,9,10]
def flatten(list):
  for i in list:
    for j in i:
      yield j
L1=[[1,2,3],[4,5],[6,7,8,9]]
flat=flatten(L1)
print (list(flat))
"""
#p8Load sample content in text file.Read data and find
def counting(filename):
  txt_file = open(filename, "r")
  vowel = 0
  line = 0
  character = 0

  # Make a vowels list so that we can
  # check whether the character is vowel or not
  vowels_list = ['a', 'e', 'i', 'o', 'u',
                 'A', 'E', 'I', 'O', 'U']

  # Iterate over the characters present in file
  for alpha in txt_file.read():

    # Checking if the current character is vowel or not
    if alpha in vowels_list:
      vowel += 1

    # Checking if the current character is
    # not vowel or new line character
    elif alpha not in vowels_list and alpha != "\n":
      character += 1

    # Checking if the current character
    # is new line character or not
    elif alpha == "\n":
      line += 1

  # Print the desired output on the console.
  print("Number of vowels in ", filename, " = ", vowel)
  print("New Lines in ", filename, " = ", line)
  print("Number of characters in ", filename, " = ", character)


# Calling the function counting which gives the desired output
counting('write_data1.txt')
with open(r"write_data1.txt", 'r') as fp:
  data=fp.read()
  line=data.split()
  count = 0
  words = 0
  lines = data.split("\n")
  for line in lines:
    count += 1
    for word in line.split(" "):
      print(word)
      words += 1
  print("Total lines, words : ",words)
