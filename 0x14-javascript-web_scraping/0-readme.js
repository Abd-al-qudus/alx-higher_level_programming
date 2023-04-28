#!/usr/bin/node
const fs = require('fs');
const filepath = process.argv[2];
fs.readFile(filepath, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  }
  console.log(data.toString());
});
