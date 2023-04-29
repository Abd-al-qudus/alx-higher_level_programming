const request = require('request');
const API = 'https://swapi-api.alx-tools.com/api/films/';
const id = process.argv[2];
const requestUrl = API + id;
request.get(requestUrl).on('response', function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (response.statusCode == 200) {
      title = JSON.parse(body).title;
      console.log(title);
    } else {
      console.log('Error code:', response.statusCode);
    }
  }
});
