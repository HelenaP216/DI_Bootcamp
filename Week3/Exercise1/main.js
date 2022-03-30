
// Exercise 1 : Move the box
//     Move the box from left to right
//     Tip: use setInterval

let animated = document.querySelector("#animate");
let distance = 0;

function moveLeft() {
    if (distance == 350) {
        distance;
    } else {
        distance++
        animated.style.left = `${distance}px` 
        console.log(animated.style.left)
    }
}

function myMove() {
    setInterval(moveLeft, 10);
}