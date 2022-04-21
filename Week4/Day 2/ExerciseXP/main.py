"""
Exercise 1 : Favorite numbers
    Create a set called my_fav_numbers with all your favorites numbers.
    Add two new numbers to the set.
    Remove the last number.
    Create a set called friend_fav_numbers with your friend’s favorites numbers.
    Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
"""

my_fav_numbers = {2, 3, 4, 7, 8}
my_fav_numbers.add(12)
my_fav_numbers.add(14)
print(my_fav_numbers)
my_fav_numbers.remove(14)
print(my_fav_numbers)

friend_fav_numbers = {3, 5, 7, 9}

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers)

 
# Exercise 2: Tuple
#    Given a tuple which value is integers, is it possible to add more integers to the tuple?
# No, one cannot add elements to a tuple because of their immutable property.


# Exercise 3: Print a range of numbers
#    Use a for loop to print all numbers from 1 to 20, inclusive.

for num in range(1, 20+1):
   print(num)


# Exercise 4: Floats
#    Recap – What is a float? What is the difference between an integer and a float?

# A float is a floating-point number = a number that has a decimal place.
# An integer is a whole number (not a fractional number) that can be positive, negative, or zero = a number without a decimal point.

#    Can you think of another way to generate a sequence of floats?

numFls = []

for num in range(1, 14):
    numFl = num / 1.0
    numFls.append(numFl)
    print(numFls)

#    Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

nums = []

for num in range(15,55,5):
    num = num / 10
    nums.append(num)

print(nums)


"""
Exercise 5: Shopping List
Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
    Remove “Banana” from the list.
    Remove “Blueberries” from the list.
    Add “Kiwi” to the end of the list.
    Add “Apples” to the beginning of the list.
    Count how many apples are in the basket.
    Empty the basket.
    Print(basket)
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.pop()
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket = []
print(basket)


# Exercise 6 : Loop
#     Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

userName = ""
myName = "Helena"

while userName != myName:
    userName = input("What's your name?")

print("Wow - same name as mine!")


# Exercise 7
#    Given a list, use a loop to print out every element which has an even index.

basket = ["Banana", "Apples", "Oranges", "Blueberries", "Soda", "Cookies"]

evenInds = []
i = 0

for i in range(0, len(basket)):
    if i % 2 == 0:
        evenInds.append(basket[i])

print(evenInds)


# Exercise 8
#    Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for num in range(1500, 2501):
    if num % 5 == 0 and num % 7 == 0:
        print(num)


"""
Exercise 9: Favorite fruits
    Ask the user to input their favorite fruit(s) (one or several fruits).
    Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
    Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    Now that we have a list of fruits, ask the user to input a name of any fruit.
        If the user's input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
        If the user's input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
"""

user_fav_fruit = input("Please write down your favorite fruit(s). Please separate fruits from each other with a single space.")

user_fav_fruit_list = list(user_fav_fruit)

user_choice_fruit = input("Please mention one fruit!")

if user_choice_fruit in user_fav_fruit_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")


# Exercise 10: Who ordered a pizza ?
#    1. Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#    2. As they enter each topping, print a message saying you’ll add that topping to their pizza.
#    3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

pizzaOrders = []
pizzaOrder = ""
pizzaPrice = 10
toppingPrice = 2.5

while pizzaOrder != "quit":
    pizzaOrders.append(pizzaOrder)
    print("I'll add " + pizzaOrder + " to your pizza.")
    pizzaOrder = input("Plz choose yr pizza toppings. To finish your order, write 'quit'")

print("Your pizza toppings are: " + ', '.join(pizzaOrders) + ", and the total price is " + str(pizzaPrice + len(pizzaOrders) * toppingPrice))


"""
Exercise 11: Cinemax
1.     A movie theater charges different ticket prices depending on a person's age.
        if a person is under the age of 3, the ticket is free.
        if they are between 3 and 12, the ticket is $10.
        if they are over the age of 12, the ticket is $15.
2.     Ask a family the age of each person who wants a ticket.
3.     Store the total cost of all the family's tickets and print it out.
4.     A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
    Write a program that asks every user for their age, and prints a list of the teens who are permitted to watch the movie.
"""

family_total = 0
input_ages = input('Enter the age of each menber of the family separated by space')
age_list = input_ages.split()

for i in range(len(age_list)):
    # convert each item to int type
    age_list[i] = int(age_list[i])

print(age_list)

for age in age_list:
    if age > 3 and age < 12:
        family_total+=10
    elif age>=12:
        family_total+=15

print(family_total)


# Exercise 12 : Who is under 16?
#    Given a list of names, write a program that asks every user for their age, if they are less than 16 years old remove them from the list.
#    At the end, print the final list.

people = ["John", "Suzy", "James", "Menachem", "Sarah"]
people_sorted = []

for individual in people: 
    age = int(input(f'what is your age {individual}? '))
    if age > 16:
        people_sorted.append(individual)
print(people_sorted)


# Exercise 13
#   1. Make a list called sandwich_orders and fill it with the names of various sandwiches .
#   2. Then make an empty list called finished_sandwiches.
#   3. As each sandwich is made, move it to the list of finished sandwiches.
#   4. After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

sandwich_orders = ["tuna", "pesto", "cheese", "plain"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'I made your {finished_sandwich} sandwich')


# Exercise 14
# Instructions
# Using the list sandwich_orders from Exercise 13, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders.extend(list(['pastrami'])*3)
print(f'Sandwich orders: {sandwich_orders}')
print('The deli has run out of pastrami\n')

sandwich_orders_len = len(sandwich_orders)
i = 1

while i < len(sandwich_orders):
    if sandwich_orders[i] == 'pastrami':
        sandwich_orders.pop(i)
    else:
        i = i +1

finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)

for finished_sandwich in finished_sandwiches:
    print(f'I made your {finished_sandwich} sandwich')
