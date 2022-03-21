
// Exercise 1:
let addressNumber;
addressNumber = 22;
console.log(addressNumber);

let addressStreet = "Ha-Hagana";
console.log(addressStreet);

let country = "Israel";

globalAddress = addressNumber + " " + addressStreet + " " + country;
console.log(globalAddress);

globalAddress2 = `${addressStreet} ${addressNumber} ${country}`
console.log(globalAddress2);

console.log("I live in " + globalAddress + ".");

// Exercise 2:
let birthYear = 1964;
let futureYear = 2024;

// After my birthday:
let myAgeAfterBirthday = futureYear - birthYear;

// Before my birthday:
let myAgeBeforeBirthday = futureYear - birthYear - 1;

console.log(`I will be ${myAgeBeforeBirthday} in ${futureYear}`);
console.log("I will be " + myAgeAfterBirthday + " in " + futureYear);


// Exercise 3:
let pets = ["cat", "dog", "fish", "rabbit", "cow"];
console.log(pets [1]);

pets.push("horse");
console.log(pets);

pets.splice(3, 1);
console.log(pets);

let length = pets.length;
console.log(length);