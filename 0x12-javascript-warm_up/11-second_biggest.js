#!/usr/bin/node

const length = process.argv.length;

if (length <= 3) {
  console.log(0);
} else {
  const argList = process.argv.map(Number).sort((a, b) => (a - b));
  console.log(argList[length - 2]);
}
