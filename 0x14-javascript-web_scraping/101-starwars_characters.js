#!/usr/bin/node
const request = require('request');
const charId = process.argv[2];
const moviesAPI = 'https://swapi-api.alx-tools.com/api/films/';

function getName (url, callback) {
  request(url, (error, resp, body) => {
    if (error) {
      console.log(error);
    } else {
      const charName = JSON.parse(body).name;
      callback(null, charName);
    }
  });
}

request(moviesAPI + charId, function (error, resp, body) {
  if (error) {
    console.log(error);
  } else {
    const charactersList = JSON.parse(body).characters;
    for (let i = 0; i < charactersList.length; i++) {
      getName(charactersList[i], (error, data) => {
        if (error) {
          console.log(error);
        }
        console.log(data);
      });
    }
  }
});
