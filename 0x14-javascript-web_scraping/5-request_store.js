#!/usr/bin/node
const process = require('process');
const request = require('request');
const fileSystem = require('fs');

const url = process.argv[2];
const path = process.argv[3];

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
    fileSystem.writeFile(path, body, 'utf8', (err, payload) => {
      if (err != null) {
        console.log(err);
      }
    });
  }
});
