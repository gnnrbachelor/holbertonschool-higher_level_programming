#!/usr/bin/node

let length = process.argv.length;

if (length <= 3) {
	console.log(0);
} else {
let argList = process.argv.map(Number).sort((a, b) => (a - b));
console.log(argList[length - 2]);
}

