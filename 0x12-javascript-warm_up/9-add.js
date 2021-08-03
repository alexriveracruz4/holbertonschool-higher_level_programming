#!/usr/bin/node
'use strict';
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (Number(a) + Number(b));
  }
}

console.log(add(a, b));
