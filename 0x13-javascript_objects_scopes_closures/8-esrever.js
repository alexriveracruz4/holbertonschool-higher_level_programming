#!/usr/bin/node
exports.esrever = function (list) {
  const r = [];
  for (let i = 0; i < list.length; i++) {
    r.unshift(list[i]);
  }
  return (r);
};
