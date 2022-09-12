#!/usr/bin/node
// script that display the status code of a GET request
const arg = process.argv;
const axios = require('axios');

axios
  .get(arg[2])
  .then(res => {
    console.log('code:', res.status);
  })
  .catch(error => {
    console.log('code:', error.response.status);
  });
