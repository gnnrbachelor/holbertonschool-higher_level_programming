#!/usr/bin/node
const fileSystem = require('fs');
const process = require('process');

const file = process.argv[2];
const body = process.argv[3];

fileSystem.writeFile(file, body, 'utf8', (err, data) => {
  if (err != null) {
    console.log(err);
  }
});
