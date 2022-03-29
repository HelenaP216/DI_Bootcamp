
// Exercise 1 : Change the article

// 1. Using a DOM property, retrieve the h1 and console.log it.

let title = document.getElementsByTagName("h1");
console.log(title);

// 2. Using DOM methods, remove the last paragraph in the <article> tag.

let parentElems = document.getElementsByTagName("article");
let childElems = document.getElementsByTagName("p");
let parentElem = parentElems[0];
parentElem.removeChild(childElems[childElems.length-1]);
console.log(parentElem)

// 3. Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

let titleH2 = document.querySelector("h2"); 
titleH2.addEventListener("click", changeColor);

function changeColor() {
    titleH2.style.backgroundColor = "red";
}

// 4. Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

let titleH3 = document.querySelector("h3");
titleH3.addEventListener("click", hideElement);

function hideElement() {
    titleH3.style.display = "none"
}

// 5. Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

let button = document.getElementsByClassName("button")[0];
let paragraphs = document.querySelectorAll("p");

button.addEventListener("click", makeBold);

function makeBold() {
    for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.fontWeight = "bold"
}
}

// Exercise 2 : Work with forms

// EXERCISE 2

// 1. Retrieve the form and console.log it.

let form = document.querySelector("form");
console.log(form);

// 2. Retrieve the inputs by their id and console.log them.

let allInputId = document.querySelectorAll("#fname, #lname, #submit");
console.log(allInputId);

// 3. Retrieve the inputs by their name attribute and console.log them.

let fname = document.getElementsByName("fname");
let lname = document.getElementsByName("lname");
console.log(fname, lname);

// 4. When the user submits the form (ie. submit event listener)
//     get the values of the input tags,
//     make sure that they are not empty,
//     create an li per input value,
//     then append them to a the <ul class="usersAnswer"></ul>, below the form.

let ulAnswers = document.querySelector(".usersAnswer");
console.log(ulAnswers);
let submit = document.querySelector("#submit");
let newFname = document.querySelector("#fname");
let newLname = document.querySelector("#lname");

submit.addEventListener("click", click);

function click(event) {
  event.preventDefault();
  let newLi = document.createElement("li");
  let newText = document.createTextNode(newFname.value);
  newLi.append(newText);
  ulAnswers.appendChild(newLi);
  let newLi2 = document.createElement("li");
  let newText2 = document.createTextNode(newLname.value);
  newLi2.append(newText2);
  ulAnswers.appendChild(newLi2);
}


// Exercise 3 : Transform the sentence


// 1. Create a global variable named allBoldItems.

let allBoldItems;

// 2. Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

let bold = document.getElementsByTagName ("strong");
let i;

function getBoldItems() {
    console.log(bold)
}
// 3. Create a function called highlight() that changes the color of all the bold text to blue.

function highlight() {
    for (i = 0; i < bold.length; i++)
    bold[1].style.color = "blue"
}

// 4. Create a function called return_normal() that changes the color of all the bold text back to black.

function return_normal() {
    for (i=0; i < bold.length; i++) {
 	bold[i].style.color = "black"
}
}

// 5. Call the function highlight() onmouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() onmouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

for (i=0; i < bold.length; i++) {
 	bold[i].addEventListener("mouseover", highlight)
 	bold[i].addEventListener("mouseout", return_normal)
}

// Exercice 4 : Volume of a sphere

const addForm = document.forms["MyForm"];

addForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const value = addForm.querySelector('input[type="text"]').value;
  let volume = (4 / 3) * Math.PI * Math.pow(value, 3);
  let result = (addForm.querySelector("#volume").value = volume);
});
