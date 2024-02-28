/* JavaScript script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello. */
const $ = window.$;
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(document).ready(function () {
  $.get(url, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
