window.initMap = function () {
    const map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 35.82216262817383, lng: 129.2528076171875 },
      zoom: 13,
    });
  };