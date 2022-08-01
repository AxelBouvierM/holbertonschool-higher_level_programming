#!/usr/bin/node
/// script that prints a square
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  let i = 0;
  for (i = 0; i < parseInt(process.argv[2]); i++) {
    let str = '';
    let x = 0;
    for (x = 0; x < parseInt(process.argv[2]); x++) {
      str += 'X';
    }
    console.log(str);
  }
}
