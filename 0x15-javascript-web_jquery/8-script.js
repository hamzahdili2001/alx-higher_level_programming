/* JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json */
const $ = window.$;
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  for (const movie of Object.values(data.results)) {
    const title = movie.title;
    $('UL#list_movies').append($('<li></li>').text(title));
  }
});
