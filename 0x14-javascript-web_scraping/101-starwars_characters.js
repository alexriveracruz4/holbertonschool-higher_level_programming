#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request.get(url, (error, response, data) => {
  if (error) console.log(error);
  else {
    const character = JSON.parse(data).characters;
    printcur(character, 0);
  }
});

function printcur (arr, idx) {
  if (idx >= arr.length) {
    return;
  }
  request.get(arr[idx], (e, r, b) => {
    if (e) console.log(e);
    else {
      console.log(JSON.parse(b).name);
    }
    return printcur(arr, idx + 1);
  });
}
