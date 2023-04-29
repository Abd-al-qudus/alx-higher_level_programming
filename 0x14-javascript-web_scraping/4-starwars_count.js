#!/usr/bin/node
const request = require('request');
const API = process.argv[2];
request(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const moviesList = JSON.parse(body).results;
    console.log(moviesList.reduce((charCount, movies) => {
      return movies.characters.find((character) => character.endsWith('/18/'))
        ? charCount + 1
        : charCount;
    }, 0));
  }
});
