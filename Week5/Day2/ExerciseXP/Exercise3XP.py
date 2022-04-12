import random

from ExerciseXP import Dog

class PetDog(Dog):
    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
    
    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self, *args):
#        dog.names = ["Tirlittan", "Sofi", "Milky"]
        print(self.name, *args, "all play together")

    def do_a_trick(self):
        while random.randint(1, 4):
            if random.randint == 1:
                print(f"{self.name} does a barrel roll.")
            elif random.randint == 2:
                print(f"{self.name} stands on his back legs.")
            elif random.randint == 3:
                print(f"{self.name} shakes your hand.")
            elif random.randint == 4:
                print(f"{self.name} dog_name plays dead.")
    
dog4 = PetDog("Tirlittan", 3, 10)
dog5 = PetDog("Sofi", 1, 6)
dog6 = PetDog("Milky", 1, 5)
