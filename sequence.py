'''Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Then, the output should be:
HELLO WORLD'''

def Capitilizer(data=''):
    return data.upper()


print(Capitilizer(input("Enter a string")))