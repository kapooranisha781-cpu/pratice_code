const input = document.createElement("input");
input.placeholder = "enter name";
const arr = input.value.split(" ").map(Number);
console.log(arr);

document.body.append(input)


