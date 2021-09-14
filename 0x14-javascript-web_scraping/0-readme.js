#!/usr/bin/node
const fileSystem = require('fs');
const process = require('process');

const file = process.argv[2];

fileSystem.readFile(file, 'utf8', (err, data) => {
  if (err != null) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
