/* JavaScript script that adds, removes and clears LI elements from a list when the user clicks */
const $ = window.$;
$(document).ready(function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').on('click', function () {
    $('UL.my_list').empty();
  });
});
