#Exercise 1 – Random Sentence Generator
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# 1. Download this word list
# 2. Save it in your development directory.
# 3. Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

import random

def get_words_from_file(file):
    with open(file, "r") as f:
        sentence = f.readlines()
        return sentence

# 4. Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
#        use the words list to get your random words.
#        the amount of words should be the value of the length parameter.
# 5. Take the random words and create a sentence (using a python method), the sentence should be lower case.

def get_random_sentence(length):
    word_li = get_words_from_file("C:\Users\paavi\Documents\WordList.txt")
    li = []
    for _ in range(length):
        x = random.choice(word_li)
        li.append(x[: -2])
    return " ".join(li).lower()


# 6. Create a function called main which will:
# 7. Print a message explaining what the program does.

def main():

    """ This program accepts integer values from 2 to 20 which then decide how long the sentence will be. """

# 8. Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
#   If the user inputs incorrect data, print an error message and end the program.
#   If the user inputs correct data, run your code.

    try:
        number_words = int(input("How long a sentence do you want? Choose number from 2 to 20, inclusive."))
        if 2 <= number_words <= 20:
            return get_random_sentence(number_words)
        else:
            return "Your number is not between 2 and 20."
    except ValueError:
        return "Not a number."

print(main.__doc__)
print(main())



# Exercise 2: Working with JSON

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# 1. Access the nested “salary” key from the JSON-string above.

dic = json.loads(sampleJson)
print(dic["company"]["employee"]["payable"]["salary"])

# 2. Add a key called “birth_date” to the JSON-string at the same level as the “name” key.

dic["company"]["employee"]["birthday"] = "1995-12-30"

print(dic)

# 3. Save the dictionary as JSON to a file.

dic = "my_file.json"

with open("data.json", "w") as f:
    json.dump(dic, f)
