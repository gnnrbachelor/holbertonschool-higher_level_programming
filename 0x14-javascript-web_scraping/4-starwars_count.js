#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

let count = 0;

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
    const payload = JSON.parse(body).results;

    for (let i = 0; i < payload.length; i++) {
      const charList = payload[i].characters;
      for (let j = 0; j < charList.length; j++) {
        const character = charList[j];
        const id = character.split('/')[5];

        if (id === '18') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
