#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const e in list) {
    if (list[e] === searchElement) {
      c++;
    }
  }
  return (c);
};
