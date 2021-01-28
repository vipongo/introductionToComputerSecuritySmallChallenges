import string
import random
#Disclaimer, I used a lot of variable. I could have used less but the name of the variable had more sense the way I did
#You can change the randomList variable to test more possibilities!
randomList = []
for i in range (20):
    randomList.append(random.randint(65,91))
    
print("RandomList is: ")
print(randomList)
letterList = []
#transform to char
for item in randomList:
    letterList.append(chr(item))

print('Letter list is: ')
print(letterList)
concatenetedString = ""

#make a single String 
for item in letterList:
    concatenetedString = concatenetedString + item
print("Concateneted String is: "+ concatenetedString)

#Make that String to Lowercase
lowercaseString = concatenetedString.lower()
print('Lowercase String is: ' + lowercaseString)


#make it a small String
smallString = ""
for i in range(2,10):
    smallString = smallString + lowercaseString[i]

#double the String
smallString = smallString + smallString

print("The small 2-10 doubled String is: " + smallString)


