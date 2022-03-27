function playTheGame() {
    let userAnswer = confirm("Would you like to play the game?");
    console.log(userAnswer);

    if (userAnswer === false) {
        alert("No problem, Goodbye");
    } else {
        alert("Great, let's play!");
        promptUser();
    }
}

        let computerNumber = Math.round(Math.floor((Math.random() * 10) + 1));

    function promptUser() {
        let userNumber = Number(prompt("Please give a number between 0 and 10."));
        console.log(computerNumber);
        console.log(userNumber);
        counter++;
    
    if (isNaN(userNumber)) {
            alert("Sorry, not a number. Goodbye!")
            return;
        } else if (userNumber < 0 || userNumber > 10) {
            alert("Sorry, it's not a good number. Goodbye!")
            return;
            } else {
                    test(userNumber, computerNumber)   
        }
    }

    let counter = 0;
function test(userNumber, computerNumber) {
    while (counter <= 3) {
    if (userNumber === computerNumber) {
        alert("WINNER!");
    } else if (userNumber > computerNumber) {
        alert("Your number is bigger then the computer's.");
        promptUser();
        counter++;
   
    } else {
        alert("Your number is smaller then the computer's.");
        promptUser();
        counter++
    }
}

    if (counter > 3) {
        alert("Out of chances - you lost");
        return;
    }
}
