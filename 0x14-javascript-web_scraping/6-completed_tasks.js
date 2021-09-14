#!/usr/bin/node
const process = require('process');
const request = require('request');

const url = process.argv[2];
const completedTasks = {};

request(url, (err, response, body) => {
  if (err != null) {
    console.log(err);
  } else {
    const payload = JSON.parse(body);

    payload.forEach((res) => {
      if (res.completed === true) {
        const userId = res.userId;
        if (!(userId in completedTasks)) {
          completedTasks[userId] = 0;
        }
        completedTasks[userId] += 1;
      }
    });
    console.log(completedTasks);
  }
});
