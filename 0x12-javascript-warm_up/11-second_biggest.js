#!/usr/bin/node
/// script that searches the second biggest integer in the list of arguments
const argv = process.argv.slice(2);
if (!argv[0] || argv.length === 1) {
  console.log(0);
} else {
  const x = argv.sort((a, b) => b - a);
  console.log(x[1]);
}
