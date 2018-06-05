//  toggles the class of the HTML tag HEADER to red (#FF0000) when the user clicks on the tag DIV#toggle_header
$('DIV#toggle_header').on('click', function () {
  if ($('header').hasClass('red')) {
    $('header').removeClass('red');
    $('header').addClass('green');
  } else {
    $('header').removeClass('green');
    $('header').addClass('red');
  }
});
