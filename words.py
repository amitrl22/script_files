
# Program to find number of words in a textfile,using filename as argument

# run command python filename.py filename.txt

import sys

if len(sys.argv) == 1:
    print "You can also give filename as a command line argument"
    filename = input("Enter Filename: ")
else:
    filename = sys.argv[1]



num_words = 0

with open(filename, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:", num_words)