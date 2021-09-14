#!/usr/bin/node
const file_system = require('fs');
const process = require('process');

let file = process.argv[2];

file_system.readFile(file, 'utf8', (err, data) => {
	if (err != null) {
	  console.log(err);
	} else {
	  process.stdout.write(data);
	}
});
