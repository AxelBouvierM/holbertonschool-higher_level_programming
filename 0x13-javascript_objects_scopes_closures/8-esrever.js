#!/usr/bin/node
exports.esrever = function (list) {
  let count = 0;
  while (count < list.length - 1) {
    list.splice(count, 0, list.pop());
    count++;
  }
  return list;
};
