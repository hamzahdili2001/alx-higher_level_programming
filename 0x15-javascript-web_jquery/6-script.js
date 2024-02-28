/* JavaScript script that updates the text of the <header> element to New Header!!! when the user clicks on DIV#update_header */
const $ = window.$;
$('DIV#update_header').on('click', function () {
  $('header').text('New Header!!!');
});
