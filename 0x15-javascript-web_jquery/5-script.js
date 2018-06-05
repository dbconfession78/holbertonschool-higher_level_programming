// adds a LI element to a list when the user clicks on the tag DIV#add_item
$('DIV#add_item').on('click', function () {
  $('ul').append('<li></li>');
});
