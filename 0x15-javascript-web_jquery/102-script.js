// fetches and prints the wind speed of user-supplied city
window.onload = function () {
  $('INPUT#btn_search').on('click', function () {
    const cityName = $('INPUT#city_search').val();
    $.ajax({
      url: 'https://query.yahooapis.com/v1/public/yql?q=select%20wind%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22:' + cityName + '%22)&format=json',
      type: 'GET',
      dataType: 'json',
      success: function (res) {
        const results = res.query.results;
        if (results === null) {
          $('DIV#wind_speed').text('');
        } else {
          $('DIV#wind_speed').text(results.channel.wind.speed);
        }
      }
    });
  });
};
