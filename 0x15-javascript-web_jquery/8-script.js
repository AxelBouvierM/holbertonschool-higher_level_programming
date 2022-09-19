$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (res) {
    $('UL#list_movies').append(res.results.map(movie => `<li>${movie.title}</li>`));
});