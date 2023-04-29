#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const API = process.argv[2];
const fileName = process.argv[3];
request(API).pipe(fs.createWriteStream(fileName));
