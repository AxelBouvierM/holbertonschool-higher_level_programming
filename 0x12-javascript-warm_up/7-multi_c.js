#!/usr/bin/node
/// script that prints x times “C is fun”
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  for (i = 0; parseInt(process.argv[2]) > i; i++) {
    console.log('C is fun');
  }
}
