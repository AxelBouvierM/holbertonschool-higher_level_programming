#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  let matriz;
  for (matriz of list) {
    if (matriz === searchElement) {
      counter++;
    }
  }
  return counter;
};
