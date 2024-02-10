var Amadeus = require('amadeus');

var amadeus = new Amadeus({
  clientId: 'xdzuHj9hKbmqTqrx4Urx4f8ABXjUaKLN',
  clientSecret: 'uDEiPydi7eZ7yhrHEuxo8ko5YkT7'
});

amadeus.shopping.flightOffersSearch.get({
    originLocationCode: 'SYD',
    destinationLocationCode: 'BKK',
    departureDate: '2022-06-01',
    adults: '2'
}).then(function(response){
  console.log(response.data);
}).catch(function(responseError){
  console.log(responseError.code);
});