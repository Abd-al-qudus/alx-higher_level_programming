#!/usr/bin/node
const request = require('request');
const API = process.argv[2];
request(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode === 200) {
      const moviesList = JSON.parse(body).results;
      let charCount = 0;
      for (const movies in moviesList) {
        const characters = moviesList[movies].characters;
        for (const charUrl in characters) {
          if (characters[charUrl].includes('18')) {
            charCount = charCount + 1;
          }
        }
      }
      console.log(charCount);
    } else {
      console.log('Error code:', response.statusCode);
    }
  }
});
