#!/usr/bin/node
/// script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop
const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const length = lines.length;
let i = 0;
for (i = 0; length > i; i++) {
  console.log(lines[i]);
}
