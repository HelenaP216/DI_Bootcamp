#Exercise 1 : Family
#    Create a class called Family and implement the following attributes:
#        members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
#        last_name : (string)
#    Initial members data:
#    [
#        {'name':'Michael','age':35,'gender':'Male','is_child':False},
#        {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#    ]
#    Implement the following methods:
#        born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
#        is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
#        a method that prints all the members of the family.

class Family():
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name

    def born(self, **new_member_info):
        new_member_info["age"] = 0
        new_member_info["is_child"] = True
        self.members.__add__(new_member_info)
        print("Congratulations on the new baby!")
        
    def is_18(self, member_name):
        for person in self.members:
            if person["name"] == member_name:
                    return person["age"] >= 18
    
    def __repr__(self):
        family_members = "The members of the family are: "
        for member in self.members:
            family_members += f'\t{member["name"]}'
        return family_members


lane = Family("Lane", [
    {"name": "Michael", "age": 35, "gender": "male", "is_child": False},
    {"name": "Sarah", "age": 32, "gender": "female", "is_child": False}])
str(lane.born(name="Shoshi", gender="female"))
print(lane.is_18("Sarah"))
print(lane)



#Exercise 2 : TheIncredibles Family
# 1.    Create a class called TheIncredibles. This class should inherit from the Family class:
#        This is no random family they are an incredible family, therefore we need to add the following keys to our dictionaries: power and incredible_name.
#        Add a method called use_power, this method should print the power of a member if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
#        Add a method called incredible_presentation which presents the family members with their incredible names and powers.
#    Look up the names of The Incredibles characters on Google and build the family (if you can’t find the correct information just improvise).
#    Print their normal presentation and their incredible presentation.
#    Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
#    Print both presentations again. Check that Baby Jack is born and that his power is showing when using the incredible representation.



family_members = Family[
    {"name": "Michael", "age": 35, "gender": "male", "is_child": False, "power": "Huge_strength", "incredible_name": "Mike the Hero"},
    {"name": "Sarah", "age": 32, "gender": "female", "is_child": False, "power": "White_magic", "incredible_name": "PlusSarah"},
]

class Incredibles(Family):
    def __init__(self, last_name, members=[]):
        super().__init__(last_name, members=members)
    
    def use_power(self, name):
        for person in self.members:
            if person["name"] == name:
                if person["age"] >= 18:
                    print(person["power"])
                else:
                    raise Exception("You do not have any power!")
    
    def incredible_presentation(self):
        for person in self.members:
            print(f"{person['name']}, your name as Incredible is {person['incredible_name']} and your power is {person['power']}.")

incredibles = Incredibles("Lane", family_members)

incredibles.incredible_presentation()
incredibles.born(name = "Shoshi", gender = "female", power = "unknown")
incredibles.incredible_presentation()
