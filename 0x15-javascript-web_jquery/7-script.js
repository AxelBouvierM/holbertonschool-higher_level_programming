$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (res) {
    $('DIV#character').text(res.name);
});