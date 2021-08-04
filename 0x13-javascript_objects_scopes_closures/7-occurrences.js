#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (let e in list) {
    if (list[e] === searchElement) {
      c++;
    }
  }
  return (c);
};
