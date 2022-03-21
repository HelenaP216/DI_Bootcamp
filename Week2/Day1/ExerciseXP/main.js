// Exercise 1: Your Favorite Food
let myFavoriteFood = ["pizza"];
let myFavoriteMeal = ["dinner"];

console.log(`I eat ${myFavoriteFood} at every ${myFavoriteMeal}.`)

// Exercise 2: Series
// Part I
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = myWatchedSeries.toString();

console.log(`I watched ${myWatchedSeriesLength} series: ${myWatchedSeriesSentence}.`)

// Part II:
let index = myWatchedSeries.indexOf("the big bang theory");
//let result = myWatchedSeries.splice (index, 1);
myWatchedSeriesNew = myWatchedSeriesSentence.replace(myWatchedSeries[index], "friends");
myWatchedSeriesNew = myWatchedSeriesNew.split(",");
console.log(myWatchedSeriesNew);
myWatchedSeriesNew.push("My Scotland");
console.log(myWatchedSeriesNew);

myWatchedSeriesNew.unshift("Jeannette");
console.log(myWatchedSeriesNew);
index = myWatchedSeriesNew.indexOf("black mirror")
myWatchedSeriesNew.splice(index, 1)
console.log(myWatchedSeriesNew);
"money heist".split("");
console.log("money heist"[2])
console.log(myWatchedSeriesNew);

// Exercise 3: The Temperature Converter

let temperatureCelsius = 10;
let temperatureFahrenheit = temperatureCelsius / 5 * 9 + 32
console.log(`${temperatureCelsius} degrees Celsius is ${temperatureFahrenheit} degrees Fahrenheit.`)

// Exercise 4: Guess the Answers #1

1.
let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
// Prediction: 55
// Actual: 55

2.
a = 2;

console.log(a+b) //second expression
// Prediction: 23
// Actual: 23

// 3. We cannot know as it has no connection with rest of the equation.

4.
console.log(3 + 4 + '5');
// Prediction: 12
// Actual: 75
// All the numbers become strings because one of them is, but first all real numbers are counted together.



// Exercise 5 : Guess the answers #2


// What is the output of each of the expressions below?


typeof(15)
console.log(typeof(15))
// Prediction: 15, number
// Actual: number

typeof(5.5)
console.log(typeof(5.5))
// Prediction: number
// Actual: number

typeof(NaN)
console.log(typeof(NaN))
// Prediction: NaN or -1
// Actual: number

typeof("hello")
console.log(typeof("Hello"))
// Prediction: string
// Actual: string

typeof(true)
console.log(typeof(true))
// Prediction: true
// Actual: boolean

typeof(1 != 2)
console.log(typeof(1 != 2))
// Prediction: true
// Actual: boolean

"hamburger" + "s"
console.log("hamburger" + "s")
// Prediction: "hamburgers"
// Actual: hamburgers

"hamburgers" - "s"
console.log("hamburgers" - "s")
// Prediction: NaN
// Actual: NaN

"1" + "3"
console.log("1" + "3")
// Prediction: 4
// Actual: 13

"1" - "3"
console.log("1" - "3")
// Prediction: -1
// Actual: -2

"johnny" + 5
console.log("johnny" + 5)
// Prediction: johnny5
// Actual: johnny5

"johnny" - 5
console.log("johnny" - 5)
// Prediction: NaN
// Actual:NaN

99 * "hello"
console.log(99 * "hello")
// Prediction: 99 * "hello"
// Actual: NaN

1 != 1
console.log(1 != 1)
// Prediction: boolean
// Actual: false

1 == "1"
console.log(1 == "1")
// Prediction: true
// Actual: true

1 === "1"
console.log(1 === "1")
// Prediction: false
// Actual: false




// EXERCISE 6

5 + "34"
console.log(5 + "34")
// Prediction: 534
// Actual: 534

5 - "4"
console.log(5 - "4")
// Prediction: 1
// Actual: 1

10 % 5
console.log(10 % 5)
// Prediction: 0
// Actual: 0

5 % 10
console.log(5 % 10)
// Prediction: 5
// Actual: 5

"Java" + "Script"
console.log("Java" + "Script")
// Prediction: JavaScript
// Actual: JavaScript

" " + " "
console.log(" " + " ")
// Prediction: "  "
// Actual:

" " + 0
console.log(" " + 0)
// Prediction: 0
// Actual: 0

true + true
console.log(true + true)
// Prediction: true
// Actual: 2

true + false
console.log(true + false)
// Prediction: 0
// Actual: 1

false + true
console.log(false + true)
// Prediction: 1
// Actual: 1

false - true
console.log(false - true)
// Prediction: -1
// Actual: -1

!true
console.log(!true)
// Prediction: 0
// Actual:false

3 - 4
console.log(3 - 4)
// Prediction: -1
// Actual: -1

"Bob" - "bill"
console.log("Bob" - "bill")
// Prediction: NaN
// Actual: NaN
