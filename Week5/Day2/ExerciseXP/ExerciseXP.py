#Exercise 1 : Pets
#Using the given code:
# 1. Create another cat breed. In order to do so, create a class which inherits from the Cat class.
# 2. Create a few cat instances.
# 3. Create a list called my_cats, which will hold all the created cat instances.
# 4. Create a variable called my_pets. It’s value is an instance of the Pet class.
#    Hint : Use the my_cats variable to create the instance.
# 5. Take all the cats for a walk, use the walk method.

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class SipooBlue(Cat):
    def chat(self, sounds):
        return f'{sounds}'

cat1 = SipooBlue('Kisu', 3)
cat2 = Chartreux('Misu', 5)
cat3 = Bengal('Matt', 1)
cat4 = Cat('Sanna', 8)

my_cats = [cat1, cat2, cat3, cat4]

my_pets = Pets(my_cats)
my_pets.walk()



#Exercise 2 : Dogs
# 1. Create a class called Dog with the following attributes name, age, weight.
# 2. Implement the following methods in the Dog class:
#        bark: returns a string which states: “<dog_name> is barking”.
#        run_speed: returns the dogs running speed (weight/age*10).
#        fight : takes a parameter which value should be another dog called other_dog, returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
# 3. Create 3 dogs and run them through your class.

class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return(f"{self.name} is barking!")
    
    def run_speed(self):
        self.run_speed = self.weight / self.age * 10
        return(self.run_speed)
    
    def fight(self, other_dog):
        run_speed1 = self.run_speed
        run_speed2 = other_dog.run_speed

        if run_speed1 > run_speed2:
            print(f"Winner is {self.name}!")
        else:
            print(f"Winner is {other_dog.name}!")

dog1 = Dog("Samson", 4, 70)
dog2 = Dog("Huahua", 1, 5)
dog3 = Dog("Brindi", 7, 15)

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(dog1.run_speed())
print(dog2.run_speed())
print(dog3.run_speed())

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))



