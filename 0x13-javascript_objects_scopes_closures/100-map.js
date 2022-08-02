#!/usr/bin/node
const lista = require('./100-data').list;
console.log(lista);
let i = 0;
const lista2 = lista.map(x => x * i++);
console.log(lista2);
