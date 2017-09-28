// fetches and replaces the name of this URL: http://swapi.co/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

const url = 'https://swapi.co/api/people/5/?format=json';
$(function () {
  $.get(url, function (data, textStatus) {
    $.getJSON(data, function () {
      const name = data.name;
      $('DIV#character').attr('name', name);
    });
  });
});
