#!/usr/bin/node
const fs = require('fs');
const arg = process.argv;
const file_1 = fs.readFileSync(arg[2]);
const file_2 = fs.readFileSync(arg[3]);
fs.writeFileSync(arg[4], file_1 + file_2);
