let map;
// global array to store the marker object 

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 33.684, lng: 73.0479},
    zoom: 12
  });


function createMarker(pos, t, color) {
    var marker = new google.maps.Marker({       
        position: pos, 
        map: map,  // google.maps.Map 
        title: t,
        icon: {
          url: "http://maps.google.com/mapfiles/ms/icons/" + color +"-dot.png"
        }      
    }); 
    google.maps.event.addListener(marker, 'click', function() { 
       window.open("/location/" + t); 
    }); 
    return marker;  
}

let marker = createMarker({lat: 33.684, lng: 73.0479}, "m1", "red");

}