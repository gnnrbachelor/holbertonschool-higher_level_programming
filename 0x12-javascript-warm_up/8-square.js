#!/usr/bin/node

const size = Math.floor(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let k = 0;
    for (let j = 0; j < size; j++) {
      process.stdout.write('X');
      k++;
    }
    if (k === size) {
      console.log();
    }
  }
}
