#1. Using the input function, ask the user for a string. The string must be 10 characters long.
#    If it’s less than 10 characters, print a message which states “string not long enough”.
#    If it’s more than 10 characters, print a message which states “string too long”.

string = input("Enter a string: ")
if len(string) < 10:
    string = input("The string is not long enough, plz try again: ")
elif len(string) > 10:
    string = input("The string is too long, plz try again: ")

#2. Then, print the first and last characters of the given text.

print(string[0], string[len(string)-1])

#3. Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. 

for i in range(len(string)):
    print(string[:i + 1])

#4. Swap some characters around then print the newly jumbled string (hint: look into the shuffle method).

from random import shuffle

string_list = list(string) # change to list as shuffle won't work on str
shuffle(string_list)
shuffled_string = ''.join(string_list) # back to str
print(shuffled_string)
