/* JavaScript script that fetches and prints how to say “Hello” depending on the language */
const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('#language_code input').text();
    $.get(url + lang, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
