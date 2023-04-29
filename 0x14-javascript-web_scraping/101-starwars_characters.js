#!/usr/bin/node
const request = require('request');
const charId = process.argv[2];
const moviesAPI = 'https://swapi-api.alx-tools.com/api/films/';

async function getName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, resp, body) => {
      if (error) {
        reject(error);
      } else {
        const charName = JSON.parse(body).name;
        resolve(charName);
        console.log(charName);
      }
    });
  });
}

async function main () {
  try {
    request(moviesAPI + charId, async function (error, resp, body) {
      if (error) {
        console.log(error);
      } else {
        const charactersList = JSON.parse(body).characters;
        for (let i = 0; i < charactersList.length; i++) {
          await getName(charactersList[i]);
        }
      }
    });
  } catch (error) {
    console.log(error);
  }
}

main();
