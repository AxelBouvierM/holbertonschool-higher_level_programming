#!/usr/bin/node
/// script that prints two arguments passed to it, in the following format: “ is ”
const arg = process.argv;
const str = arg[2] + ' is ' + arg[3];
console.log(str);
