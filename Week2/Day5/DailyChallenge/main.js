let bottlesCurr = 0;
let downBottles = 0;
let bottlesAfter = 0;
let bottlesPrompt = Number(prompt("Give a number of bottles"))
let counter = 0;
let pronoun = " "


function removeBottles() {
while (counter === 0) {
let bottlesStart = bottlesPrompt
bottlesCurr = bottlesStart;
console.log(bottlesCurr)
console.log(bottlesStart)
downBottles = downBottles + 1;
console.log(downBottles)
bottlesAfter = bottlesCurr - downBottles;
console.log(bottlesAfter)
counter++
console.log(counter)
console.log(`${bottlesCurr} bottles of beer on the wall \n ${bottlesCurr} bottles of beer \n Take ${downBottles} down, pass it around \n ${bottlesAfter} bottles of beer on the wall.`)
} 
while (counter > 0 && bottlesAfter > 0) {
bottlesCurr = bottlesAfter;
console.log(bottlesCurr)
downBottles = downBottles + 1;
console.log(downBottles)
bottlesAfter = bottlesCurr - downBottles;
if (bottlesCurr < downBottles) {
    downBottles = bottlesCurr
}
if (bottlesAfter < 0) {
    bottlesAfter = 0
}
console.log(bottlesAfter)
counter++
if (downBottles > 1) {
    pronoun = "them"
} else {
    pronoun = "it"
}
console.log(counter)
console.log(`${bottlesCurr} bottles of beer on the wall \n ${bottlesCurr} bottles of beer \n Take ${downBottles} down, pass ${pronoun} around \n ${bottlesAfter} bottles of beer on the wall.`)
}
}
removeBottles()
