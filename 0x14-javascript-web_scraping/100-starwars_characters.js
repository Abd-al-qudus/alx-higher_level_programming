#!/usr/bin/node
const request = require('request');
const charId = process.argv[2];
const moviesAPI = 'https://swapi-api.alx-tools.com/api/films/';
request(moviesAPI + charId, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersList = JSON.parse(body).characters;
    for (let i = 0; i < charactersList.length; i++) {
      request(charactersList[i], (error, resp, body) => {
        if (error) console.log(error);
        else console.log(JSON.parse(body).name);
      });
    }
  }
});
