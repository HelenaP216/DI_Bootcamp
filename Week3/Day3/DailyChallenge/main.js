// Daily challenge : Show only the letters

//     Create an input type text that takes/shows only letters. (ie. numbers and special characters won’t be accepted)

//     Hint: use one of the following events to remove any character that is not a letter
//         keyup event
//         or keypress event
//         or keydown event
//         or input event

//     Hint : Check out keycodes in Javascript or Regular Expressions

function Validate(event) {
    var KeyCode = event.KeyCode || event.which;
    var error = document.getElementById("error");
    error.innerHTML = "";
    var regExp = /^[A-Za-z]+$/;
    var isValid = regExp.test(String.fromCharCode(KeyCode));
    if (!isValid) {
        error.innerHTML = "Please use only letters";
    }
    return isValid;
}

