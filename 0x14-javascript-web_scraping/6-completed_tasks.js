#!/usr/bin/node
const request = require('request');
const API = process.argv[2];
request(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } 
  else {
    const totalTasks = JSON.parse(body);
    const completed = {};
    for (const item in totalTasks){
      const task = totalTasks[item];
      if (task.completed){
        if (completed[task.userId]){
          completed[task.userId]++;
        }
        else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});