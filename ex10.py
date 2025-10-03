###############################################################################
#  Program Name   : ex10.py
#  Author         : Samantha. F
#  Task           : (Create a program that asks for 3 friends’ names, stores them in a list, and prints them all.)
###############################################################################
friends = []
# Ask for 3 friends' names
for i in range(3):
    name = input("Enter a friend's name:")
    #friends.append(name)
# Print all friends' names
print("Your friends are:")
for friend in friends:
    print(friend)
