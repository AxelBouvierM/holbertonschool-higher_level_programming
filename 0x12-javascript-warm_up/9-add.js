#!/usr/bin/node
/// script that prints the addition of 2 integers
function add (a, b) {
  return a + b;
}
if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(NaN);
} else {
  const arg = process.argv;
  console.log(add(parseInt(arg[2]), parseInt(arg[3])));
}
