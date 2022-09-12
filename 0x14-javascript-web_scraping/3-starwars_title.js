#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer
const arg = process.argv;
const axios = require('axios');
const url = 'https://swapi-api.hbtn.io/api/films/' + arg[2];

axios
  .get(url)
  .then(res => {
    console.log(res.data.title);
  })
  .catch(error => {
    console.log('code:', error.response.status);
  });
