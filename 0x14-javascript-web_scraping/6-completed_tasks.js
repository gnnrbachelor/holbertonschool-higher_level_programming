#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const path = process.argv[3];
const completed_tasks = {};

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
	payload = JSON.parse(body);	
	
	payload.forEach((res) => {
		if (res['completed'] === true) {
			let userId = res['userId'];
			if (!(userId in completed_tasks)) {
				completed_tasks[userId] = 0;
			} 
			completed_tasks[userId] += 1;
		}
	});
	console.log(completed_tasks);
  }
});
