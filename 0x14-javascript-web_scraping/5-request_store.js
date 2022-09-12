#!/usr/bin/node
const arg = process.argv;
const axios = require('axios');
const fs = require('fs');

axios
  .get(arg[2])
  .then(res => {
    fs.writeFile(arg[3], res.data, (error) => {
      if (error) {
        console.error(error);
      }
    });
  })
  .catch(error => {
    console.log('code:', error);
  });
