#!/usr/bin/node
const request = require('request');
const charId = process.argv[2];
const API = 'https://swapi-api.alx-tools.com/api/people/';
request(API, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const people = JSON.parse(body).results;
    for (const character in people) {
      const films = people[character].films;
      for (const charIndexLink in films) {
        const indexes = films[charIndexLink];
        for (const links in indexes) {
          if (links.includes(charId.toString)) {
            console.log(people[character].name);
          }
        }
      }
    }
  }
});
