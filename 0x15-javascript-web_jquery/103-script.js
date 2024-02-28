/* JavaScript script that fetches and prints how to say “Hello” depending on the language */
const $ = window.$;
let url = 'https://fourtonfish.com/hellosalut/?lang=';
$(document).ready(function () {
  $('INPUT#language_code').on('keypress', function (e) {
    if (e.keyCode === 13) { $('INPUT#btn_translate').click(); }
  });
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    url = url + lang;
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
