let wordList = prompt("Please enter several words separated by comma.")
let words = [wordList.split(",")];
console.log(words);

function longestString() {
    let longestWord = "";
    for (let i = 0; i < words.length; i++) {
        if (longestWord.length < words[i].length) {
            longestWord = words[i];
        }
    }
    return longestWord;
}
let longestWordLength = longestString(words).length;

let starCode = "";
let starRow = "";
for(let i = 0; i<longestWordLength+4; i++){
    starRow += "*";
}


for(let i = 0; i<words.length; i++){
    let currWord = words[i];
    let printRow = "* " + currWord;
    let space = longestWordLength - currWord.length;
    for(let j = 0; j < space; j++){
        printRow += " ";
    }
    starCode += printRow + " *"+"\n";
}
console.log(starRow + "\n" + starCode + starRow);
