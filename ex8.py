###############################################################################
#  Program Name   : ex8.py
#  Author         : Samantha. F
#  Task           : (Create a program that keeps on asking the user for words until they type exit.)
###############################################################################

#This is where I ask the user for their words.

while True:
    word = input("Enter a word (type 'exit' to quit):")
    if word == "exit":
        print("Goodbye!")
        break
    else:
        print("You entered:", word)
