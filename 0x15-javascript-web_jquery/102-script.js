// fetches and prints the wind speed of user-supplied city

window.onload = function () {
  $('INPUT#btn_search').on('click', function () {
    const city = $('INPUT#city_search').val();
    console.log(city);
    $.ajax({
      url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + city + '%22)&format=json',
      type: 'GET',
      dataType: 'json',
      success: function (res) {
        const speed = res.query.results.channel.wind.speed;
        $('DIV#wind_speed').text(speed);
      }
    });
  });
};
