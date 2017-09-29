// allows user to add, remove and clear all  LI elements
window.onload = function () {
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<LI>Item</LI>');
  });

  $('DIV#remove_item').on('click', function () {
    $('UL.my_list LI').last().remove();
  });

  $('DIV#clear_list').on('click', function () {
    $('UL.my_list LI').remove();
  });
};
