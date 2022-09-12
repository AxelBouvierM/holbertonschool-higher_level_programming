#!/usr/bin/node
// script that writes a string to a file
const arg = process.argv
const fs = require('fs');

fs.writeFile(arg[2], arg[3], function(error) {
    if (error) {
        return console.error(error);
    }
});