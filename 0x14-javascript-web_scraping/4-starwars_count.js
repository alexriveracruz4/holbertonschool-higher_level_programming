#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }
  const results = JSON.parse(body).results;
  let count = 0;
  for (const i in results) {
    const chars = results[i].characters;
    for (const c in chars) {
      if (chars[c].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
