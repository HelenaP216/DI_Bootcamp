# Exercise 1 : Hello World
# Print the following output in one line of code:

print("Hello world \nHello world \nHello world \nHello world")

# Exercise 2 : Some Math
# Write code that calculates the result of: (99^3) * 8 (99 to the power of 3 times 8)

print(99 ** 3 * 8)

# Exercise 3 : What is the output ?
# Predict the output of the following code snippets:

5 < 3
print("The output of 5 < 3 is false.") 

3 == 3
print("The output of 3 == 3 is true.")

3 == "3"
print("The output of 3 == '3' is false.")

"3" > 3
print("The output of '3' > 3 is false.") #NO, THE WHOLE COMPARISON IS IMPOSSIBLEAUSE "3" IS STRING AND 3 IS A NUMBER -> INCOMMENSURABLE

"Hello" == "hello"
print("The output of 'Hello' == 'hello' is false.")


# Exercise 4 : Your computer brand
#    Create a variable called computer_brand which value is the brand name of your computer.
#    Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Dell"
print(f"I have a {computer_brand} computer.")


# Exercise 5 : Your information
#    Create a variable called name, and set it’s value to your name.
#    Create a variable called age, and set it’s value to your age.
#    Create a variable called shoe_size, and set it’s value to your shoe size.
#    Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
#    Have your code print the info message.
#    Run your code

name = "Helena"
age = "15"
shoe_size = "39"
info = f"My name is {name}. I am {age}, but it bothers me less than my shoe size which is {shoe_size}."
print(info)


# Exercise 6 : A & B
#    Create two variables, a and b.
#    Each variables value should be a number.
#    If a is bigger then b, have your code print Hello World.

a = 8
b = 7
if a > b:
    print("Hello world!")


#Exercise 7 : Odd or Even
#    Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Please give a number"))
if num % 2 == 0:
    print("num is even")
else: 
    print("num is odd")


# Exercise 8 : What’s your name ?
#    Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

name1 = input("What is your name?")
name2 = "Helena"
if name1 == name2:
    print("Surprise, surprise - I found an extra twin for you! She has even the same name as you!")
else:
    print("You two have different names - I always said there is none like you!")


# Exercise 9 : Tall enough to ride a roller coaster
# Instructions
#    Write code that will ask the user for their height in inches.
#    If they are over 145cm print a message that states they are tall enough to ride.
#    If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("How tall are you in cm?"))
if height > 145:
    print("YOu are tall enough to join the roller coaster ride!")
else:
    print("Sorry, you cannot come, you need to grow first some more!")
