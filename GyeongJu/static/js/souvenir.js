function initMap() {
  // Coordinates for the center of the map
  var center = { lat: 35.8405942,  lng: 129.2134083 }; // New York City coordinates as an example

  // Create a new map object, specifying the DOM element for display
  var map = new google.maps.Map(document.getElementById('googleMap'), {
    center: center, // Set the center of the map
    zoom: 15 // Set the zoom level
  });

  const infowindow = new google.maps.InfoWindow();
  
  shopLocations.forEach(function(shopLocation) {
    var marker = new google.maps.Marker({
      position: { lat: shopLocation.lat, lng: shopLocation.lng },
      map: map,
      title: shopLocation.shop.name // Assuming ShopLocation has a 'shop' property
    });
    
    var contentString = '<div id="content" style="width: 200px; height: 120px; overflow: hidden;">'+
    '<p style="margin: 5px;"> <b>' + shopLocation.shop.name + '</b></p>'+
    '<div style="display: flex; height: 100%;">'+
    '<div style="flex: 1;">'+
    '<img src="' + shopLocation.shop.image + '" alt="' + shopLocation.shop.name + '" style="max-width: 100px; max-height: 100px;">'+
    '</div>'+
    '<div style="flex: 2; margin-left: 10px;">'+
    '<div id="bodyContent">'+
    '<p style="margin: 0;"><strong>영업시간:</strong></p> ' + 
    shopLocation.shop.business_hours 
    '</div>'+
    '</div>'+
    '</div>'+
    '</div>';

      var infowindow = new google.maps.InfoWindow({
        content: contentString
      });

      marker.addListener('click', function() {
        map.panTo(marker.position);
        infowindow.open(map, marker);
      });

    });
};