#!/usr/bin/node
const request = require('request');
const API = process.argv[2];
request.get(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const moviesList = JSON.parse(body).results;
    console.log(moviesList.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  } else {
    console.log('Error code:', response.statusCode);
  }
});
