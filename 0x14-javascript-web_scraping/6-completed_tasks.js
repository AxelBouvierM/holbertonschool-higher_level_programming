#!/usr/bin/node
// script that computes the number of tasks completed by user id
const arg = process.argv;
const axios = require('axios');

axios
  .get(arg[2])
  .then(res => {
    const dict = {};
    for (const task of res.data) {
      if (task.completed) {
        if (task.userId in dict) {
          dict[task.userId]++;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    console.log(dict);
  })
  .catch(error => {
    console.log('code:', error);
  });
