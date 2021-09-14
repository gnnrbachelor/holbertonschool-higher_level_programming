#!/usr/bin/node
const process = require('process');
const request = require('request');

const  url = process.argv[2];

request(url, (err, response, body) => {
	if (err != null) {
		console.log(err);
	} else {
		console.log('code:', response.statusCode);
	}
});



