// Exercise 1 : List of people

// let people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review about arrays

let people = ["Greg", "Mary", "Devon", "James"];

//     Write code to remove “Greg” from the people array.

people.shift();
console.log(people);

//     Write code to replace “James” to “Jason”.

people.indexOf("James");
console.log(people.indexOf("James"));

people[people.indexOf("James")] = "Jason"
console.log(people);

//     Write code to add your name to the end of the people array.

people.push("Helena");
console.log(people);

//     Write code that console.logs Mary’s index. take a look at the indexOf method on Google.

console.log(people.indexOf("Mary"));

//     Write code to make a copy of the people array using the slice method.
//         The copy should NOT include “Mary” or your name.
//         Hint: remember that now the people array should look like this let people = ["Mary", "Devon", "Jason", "Yourname"];
//         Hint: Check out the documentation for the slice method

let newPeople = people.slice(1, 3);
console.log(newPeople);

//     Write code that gives the index of “Foo”. Why does it return -1 ?
people.indexOf("foo");
console.log(people.indexOf("foo"));
// BECAUSE THE ELEMENT "FOO" DOES NOT EXIST

//     Create a variable called last which value is the last element of the array.
//     Hint: What is the relationship between the index of the last element in the array and the length of the array?

let last = people.splice(people.length - 1);
console.log(last);

// Part II - Loops

//     Using a loop, iterate through the people array and console.log each person.

for (let i = 0; i < people.length; i++) {
    console.log(people[i])
}

//     Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
//     Hint: take a look at the break statement in the lesson.

for (let i = 0; i < people.length; i++) {
    if (i === (people.indexOf("Jason") + 1)) {
        break
    }
    console.log(people[i])
}


// Exercise 2 : Your favorite colors

//     Create an array called colors where the value is a list of your five favorite colors.
//     Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
//     Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
//     Hint : create an array of suffixes to do the Bonus

let colors = ["green", "yellow", "red", "blue", "brown"];
for (let i = 0; i < colors.length; i++) {
    console.log(`My #${i + 1} choice is ${colors[i]}.`)
}


// Exercise 3 : Repeat the question

//     Prompt the user for a number.
//     Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

let i;

do {
    i = prompt("Please give a number.");
}

while (i < 10)

//     While the number is smaller than 10 continue asking the user for a new number.
//     Tip : Which while loop is more relevant for this situation?



// Exercise 4 : Building Management

let building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent: {
        sarah: [3, 990],
        dan: [4, 1000],
        david: [1, 500],
    },
}

// Console.log the number of floors in the building.

console.log(`The number of floors in the building is ${building.numberOfFloors}.`);

// Console.log how many apartments are on the floors 1 and 3.

console.log(`There are ${building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor} rooms in the floors 1 and 3.`)

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

console.log(`${building.nameOfTenants[1]} has ${building.numberOfRoomsAndRent.dan[0]} rooms.`)

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.

if ((building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1]) > building.numberOfRoomsAndRent.dan[1]) {
    building.numberOfRoomsAndRent.dan[1] = 1200
}
console.log(`Rents of Sarah and Dan are together more than rent of Dan. Dan will have to start paying ${building.numberOfRoomsAndRent.dan[1]}.`)



// Exercise 5 : Family

// Create an object called family with a few key value pairs.
// Using a for loop, console.log the keys of the object.
// Using a for loop, console.log the values of the object.

let family = {
    numberOfChildren: 5,
    placeOfResidence: "New York",
    levelOfSatisfaction: 9.5,
    amountOfComputers: 4
}

for (let key in family) {
    console.log(key)
}

for (let key in family) {
    console.log(family[key])
}


// Exercise 6

let details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
}

// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”

for (let key in details) {
    console.log(`My ${details.my} is ${details.is} the ${details.the}.`)
}


// Exercise 7 : Secret Group

let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

//     A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
//     Hint: a string is an array of letters
//     Console.log the name of their secret society. The output should be “ABJKPS”

let sorted = names.sort()
console.log(names.sort())
console.log(sorted.length)

let societyName = "";
for (i = 0; i < sorted.length; i++) {
    societyName += names[i][0]
}
console.log(societyName)