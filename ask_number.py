'''Ask for a number (n) as an input from user. Using the use input (n), write a program to generate a dictionary that contains (i, i*i) where i is key and i*i is a value for numbers between the range 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}'''

square = dict()

number = int(input("Enter a number"))

i = 1
while i <= number:
    square.update({i: i * i})
    i = i + 1

print(square)