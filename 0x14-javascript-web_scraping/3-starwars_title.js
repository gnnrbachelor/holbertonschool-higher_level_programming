#!/usr/bin/node
const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
let json;

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
    json = JSON.parse(body);
    console.log(json.title);
  }
});
