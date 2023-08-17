/* Loops */
/* 

for(iterador; condition; increment){
    sentences
}

for(valor of collection){
    sentences
}

for(index in collection){
    sentences
}

while(condition){
    sentences
}

do {
    sentences
} while (condition)


*/

let nombres = ["Hugo", "Paco", "Luis"];

for(let i = 1; i <= 10; i++){ // i += 1, i = i + 1
    console.log(i)
}

for (let i = 0; i < nombres.length; i++){
    console.log(nombres[i])
}

let i = 0;
while(i < nombres.length){
    console.log(nombres[i])
    i++;
}