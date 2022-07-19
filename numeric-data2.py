#introducing the string data type
ritasString = "This is introducing data string."
print(ritasString)
print(type(ritasString))
print(ritasString + " is of the data type " + str(type(ritasString)))

#Working with string concatenation

firstString = "There is an"
secondString = "uprise in the middle east"
thirdString = firstString + secondString
print(thirdString)

#Working with input strings
name = input("What is your name? ")
print(name)

#format output string
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print()

print("{}, you like a {} {}".format(name,color,animal))


