#Instructions : Old MacDonald’s Farm
#    Take a look at the following code and output:
#File: market.py
#macdonald = Farm("McDonald")
#macdonald.add_animal('cow',5)
#macdonald.add_animal('sheep')
#macdonald.add_animal('sheep')
#macdonald.add_animal('goat', 12)
#print(macdonald.get_info())

#Output

#McDonald's farm
"""
cow : 5
sheep : 2
goat : 12
    E-I-E-I-0!
"""
#Create the code that is needed to receive the result provided above. Below are a few questions to assist you with your code:
#1. Create a class called Farm. How should it be implemented?
#2. Does the Farm class need an __init__ method? If so, what parameters should it take?

class Farm():
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal, amount_of_animals):
        if animal in self.animals: 
            self.animals[animal] += amount_of_animals
        else:
            self.animals[animal] = amount_of_animals

    def get_info(self):
        print(f"{self.name}""'s Farm".center(22))
        for animal in self.animals:
            print(f"{animal} : {self.animals[animal]}")
            print("E-I-E-I-O!")
    
    def get_animal_types(self):
        return sorted(list(self.animals))

    def get_short_info(self):
        print(f"{self.name}'s farm has {','.join(self.get_animal_types())}.")

#3. How many methods does the Farm class need?
#4. Do you notice anything interesting about the way we are calling the add_animal method? What parameters should this function have? How many…?
#5. Test your code and make sure you get the same results as the example above.

macdonald=Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("goat", 12)
macdonald.get_info()
macdonald.get_short_info()

# Change something