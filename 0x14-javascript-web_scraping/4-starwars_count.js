#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];

let count = 0;

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
	payload = JSON.parse(body).results;
	
	for (let i = 0; i < payload.length; i++) {
		let char_list = payload[i].characters;
		for (let j = 0; j < char_list.length; j++) {
			let character = char_list[j];
			let id = character.split('/')[5];
			
			if (id === '18') {
				count += 1;
			}
		}
  }
	console.log(count);
}
});
