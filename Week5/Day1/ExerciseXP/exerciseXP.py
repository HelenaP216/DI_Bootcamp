#Exercise 1: Cats
#    Instantiate three Cat objects using the code provided above.
#    Outside of the class, create a function that finds the oldest cat and returns the cat.
#    Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("Milky", 2)
cat2 = Cat("Silky", 2.5)
cat3 = Cat("Sunny", 7)

cat_list = [cat1, cat2, cat3]

#print(cat1.age)
#print(cat1.name)

def oldest_cat(cats2):
    oldest = cats2[0]
    for cat in cats2:
        if cat.age > oldest.age:
            oldest = cat
    return oldest

oldest = oldest_cat(cat_list)
print(f"The oldest cat is {oldest.name}, and she is {oldest.age} years old.")


#Exercise 2: Dogs
# 1. Create a class called Dog.
# 2. In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.

class Dog():
    def __init__(self, name, height):
        self.name = name
        self.height = height

# 3. Create a method called bark that prints the following string “<dog_name> goes woof!”.

    def bark(self):
        print(f"{self.name} goes woof!")

# 4. Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    
    def jump(self):
        x = self.height + 20
        print(f"{self.name} jumps {x} cm high!")

# 5. Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.

davids_dog = Dog("Rex", 50)

# 6. Print the details of his dog (ie. name and height) and call the methods bark and jump.

print(f"David's dog is called {davids_dog.name}, and it is {davids_dog.height} cm high.")
davids_dog.bark()
davids_dog.jump()

# 7. Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.

sarah_dog = Dog("Teacup", 20)

# 8. Print the details of her dog (ie. name and height) and call the methods bark and jump.

print(f"Sarah's dog is called {sarah_dog.name}, and its height is {sarah_dog.height} cm.")
sarah_dog.bark()
sarah_dog.jump()

# 9. Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
if sarah_dog.height > davids_dog.height:
    print(f"{sarah_dog.name} is bigger!")
elif davids_dog.height > sarah_dog.height:
    print(f"{davids_dog.name} is bigger!")
else:
    print(f"{sarah_dog.name} and {davids_dog.name} are of same height!")


#Exercise 3 : Who’s the song producer?
# 1. Define a class called Song, it will show the lyrics of a song.
#    Its __init__() method should have two arguments: self and lyrics (a list).
# 2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# 3. Create an object, for example:
#    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# 4. Then, call the sing_me_a_song method. 

class Song():
    def __init__(self, lyrics = []):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line, end="\n")

stairway = Song(["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"])
stairway.sing_me_a_song()


#Exercise 4 : Afternoon at the Zoo
# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# 3. It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# 4. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# 5. Create a method called get_animals that prints all the animals of the zoo.
# 6. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# 7. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
#    Example
"""    { 
        1: "Ape",
        2: ["Baboon", "Bear"],
        3: ['Cat', 'Cougar'],
        4: ['Eel', 'Emu']
    }
    """
# 8. Create a method called get_groups that prints the animal/animals inside each group.
# 9. Create an object called ramat_gan_safari and call all the methods.
#    Tip: The zookeeper is the one who will use this class.
#    Example
#    Which animal should we add to the zoo --> Giraffe
#    x.add_animal(Giraffe)

# 1. Create a class called Zoo.
# 2. In this class create a method __init__ that takes one parameter: zoo_name.
# 3. It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo():
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

# 4. Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.

    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

# 5. Create a method called get_animals that prints all the animals of the zoo.

    def get_animals(self):
        print("The animals currently in the zoo: ")
        animal_list = ""
        for animal in self.animals:
            animal_list = animal_list + animal 
        return animal_list

# 6. Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            del self.animals[self.animals.index(animal_sold)]

# 7. Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.

    def sort_animals(self):
        sorted_animals = sorted(self.animals)
        if len(sorted_animals):
            animal_dict = {}
            current_key = 1
            last_letter = "A"
            for animal in sorted_animals:
                current_letter = animal[0]
                if last_letter < current_letter:
                    last_letter = current_letter
                    if current_key in animal_dict:
                        if type(animal_dict[current_key]) == list:
                            animal_dict[current_key].append(animal)
                        else:
                            animal_dict[current_key] = [animal_dict[current_key]]
                            animal_dict[current_key].append(animal)
                    else:
                        animal_dict[current_key] = animal
                return animal_dict
            else:
                print("Nothing to sort")

# 8. Create a method called get_groups that prints the animal/animals inside each group.

    def get_groups(self):
        animal_dict = self.sort_animals()
        for letter_idx in animal_dict:
            item = animal_dict[letter_idx]
            if type(item) == list:
                letter = item[0][0]
            else:
                letter = item[0]
            print(letter+": ", end="")
            print(animal_dict[letter_idx])

# 9. Create an object called ramat_gan_safari and call all the methods.
#    Tip: The zookeeper is the one who will use this class.


ramat_gan_safari = Zoo("Ramat Gan Safari")

animals_to_add_to_zoo = ["tiger", "sea horse", "gazelle", "emu", "equus", "tarantula", "tapir", "tortoise"]
for animal in animals_to_add_to_zoo:
    ramat_gan_safari.animals.add_animal(animal)

ramat_gan_safari.animals.get_animals()
ramat_gan_safari.animals.sell_animal("gazelle")
ramat_gan_safari.animals.sort_animals()
ramat_gan_safari.animals.get_groups()
ramat_gan_safari.animals.get_animals()

