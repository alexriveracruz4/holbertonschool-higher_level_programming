#!/usr/bin/node
'use strict'
const l = process.argv[2];
if (isNaN(l)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < l; i++) {
    console.log('X'.repeat(l));
  }
}
