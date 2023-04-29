#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const API = process.argv[2];
const fileName = process.argv[3];
request(API, function(error, response, body){
  if (error) {
    console.log(error);
  }
  else{
    fs.writeFile(fileName, body, 'utf-8');
  }
});
