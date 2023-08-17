/* Conditionals */
/* 

if(condition){
    sentences
}

if(condition){
    sentences
} else {
    sentences
}

if (condition) {
    sentences
} else if (condition) {
    sentences
} else {
    sentences
}


switch(valor){
    caso x:
        sentences
        break;

    default:
        sentences
        break;
}


*/

let a = 6;
let b = 7;
let c = 4;


if (a > b) {
    console.log(a)
}


if (a > c) {
    console.log(a)
} else {
    console.log(c)
}

if (a > b && a > c) {
    console.log("A")
} else if (b > c) {
    console.log("B")
} else {
    console.log("C")
}