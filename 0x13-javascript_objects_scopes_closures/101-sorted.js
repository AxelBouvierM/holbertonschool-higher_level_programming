#!/usr/bin/node
const dic = require('./101-data.js').dict;
const tmp = {};
for (const key in dic) {
  if (tmp[dic[key]] === undefined) {
    tmp[dic[key]] = [];
  }
  tmp[dic[key]].push(key);
}
console.log(tmp);
