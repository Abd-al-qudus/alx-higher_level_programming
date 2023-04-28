#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const filecontent = process.argv[3];
fs.writeFile(filename, filecontent, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
