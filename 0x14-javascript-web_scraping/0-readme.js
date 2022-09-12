#!/usr/bin/node
// script that reads and prints the content of a file
const filename = process.argv;
const fs = require('fs');

fs.readFile(filename[2], 'utf-8', function (error, data) {
  if (error) {
    return console.log(error);
  }
  console.log(data.toString());
});
