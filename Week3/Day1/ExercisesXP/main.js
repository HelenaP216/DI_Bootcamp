// Exercise 1 : Change the navbar


// 1. In the <div> above, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

let newDiv = document.getElementById("navBar");
newDiv.setAttribute("id", "socialNetworkNavigation");

// 2. We are going to add a new <li> to the <ul>.
//     First, create a new <li> tag (use the createElement method).
//     Create a new text node with “Logout” as its specified text.
//     Append the text node to the newly created list node (li).
//     Finally, append this updated list node to the unordered list above, using the appendChild method.

let liNew = document.createElement("li");
let textLi = document.createTextNode("Logout");

liNew.appendChild(textLi);

let ul = document.getElementsByTagName("ul");
ul.appendChild(liNew);

// 3. Bonus
//     Use the firstElementChild and the lastElementChild properties to retrieve the first and last li elements from their parent element (ul). Display the text of each link. (Hint: use the textContent property).

let firstLi = document.ul.firstElementChild;
let lastestLi = document.ul.lastElementChild;


// Exercise 2 : Users

// 1. In the HTML above change the name “Pete” to “Richard”.

let container = document.getElementById("container");
let ulLists = document.getElementsByClassName("list");
let lastestLi = document.ulLists[0].lastElementChild
let text = lastestLi.textContent = "Richard"

// 2. Change each first name of the two <ul>'s to your name.

let firstName = document.ulLists.firstElementChild;
for (i = 0; i < ulLists.lenght; i++) {
let text2 = firstName.textContent = "Helena"
}

// 3. At the end of each <ul> add a <li> that says “Hey students”.
// Delete the name Sarah from the second <ul>.
// Bonus
//     Add a class called student_list to both of the <ul>'s.
//     Add the classes university and attendance to the first <ul>.

let lists = document.getElementsByClassName("list");//1
for(let i = 0; i <listn.length; i++) //3
{
    let newLi = document.createElement("li");
    let node = document.createTextNode("Hey students");
    newLi.appendChild(node)
    lists[i].append(newLi)
}
let secondList = lists[1] //4
let sarah = secondList.children[1]
secondList.removeChild(sarah)
