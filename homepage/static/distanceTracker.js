
/* The goal of this distance tracker is to compare the user's current location with the location of all of the dining halls to
pick the closest dining hall to them. This newest version doesn't require a google API key.
*/

// Let's check to make sure we're actually running our file...
//console.log("distanceTracker.js is running");

// Check if the user's browser supports Geolocation
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    // Handle error if Geolocation is not supported
    alert("Geolocation is not supported by this browser.");
}

function showPosition(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    // Call function to calculate and display the closest dining halls
    getClosestDiningHalls(latitude, longitude);
}

var diningHalls = [
    { name: "Commons Dining Hall", latitude: 42.72855127771457, longitude: -73.67437774248803 },
    { name: "Russell Sage Dining Hall", latitude: 42.72978947200118, longitude: -73.67806960678168 },
    { name: "BARH Dining Hall", latitude: 42.731209458978554, longitude: -73.67131895095905},
    { name: "Blitman Dining Hall", latitude: 42.73237220304262, longitude: -73.68590039328933},
];

function getClosestDiningHalls(userLat, userLon) {
    diningHalls.forEach(function(hall) {
        var distance = haversineDistance(userLat, userLon, hall.latitude, hall.longitude);
        hall.distance = distance * 0.621371; // Converting this to miles
    });

    // Sort the dining halls by distance
    // diningHalls.sort(function(a, b) {
    //     return a.distance - b.distance;
    // });

    // Call function to display the sorted dining halls on the website
    console.log("hi");
    displayDiningHalls();
}

function haversineDistance(lat1, lon1, lat2, lon2) {
    var R = 6371; // Radius of the earth in km
    var dLat = deg2rad(lat2-lat1);  
    var dLon = deg2rad(lon2-lon1); 
    var a = 
        Math.sin(dLat/2) * Math.sin(dLat/2) +
        Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) * 
        Math.sin(dLon/2) * Math.sin(dLon/2)
    ; 
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a)); 
    var d = R * c; // Distance in km
    return d;
}

function deg2rad(deg) {
  return deg * (Math.PI/180)
}

function displayDiningHalls() {
    console.log("hi");
    var commons_distance = '<p class="dynamic-text">' + 'Distance: ' + diningHalls[0].distance.toFixed(2) + ' mi away</p>';
    var sage_distance = '<p class="dynamic-text">' + 'Distance: ' + diningHalls[1].distance.toFixed(2) + ' mi away</p>';
    var barh_distance = '<p class="dynamic-text">' + 'Distance: ' + diningHalls[2].distance.toFixed(2) + ' mi away</p>';
    var blitman_distance = '<p class="dynamic-text">' + 'Distance: ' + diningHalls[3].distance.toFixed(2) + ' mi away</p>';

    var output = '';
    diningHalls.forEach(function(hall, index) {
        output += '<p class="dynamic-text">' + hall.name + ': ' + hall.distance.toFixed(2) + ' mi away';
        // If the dining hall is the first one in the list (i.e., the closest one)
        if (index === 0) {
            output += ' <span style="color: green;">(closest)</span>';
        }
        output += '</p>';
    });

    // Injecting the dynamic content into the HTML
    document.getElementById('output').innerHTML = output;
    document.getElementById('commons_distance').innerHTML = commons_distance;
    document.getElementById('sage_distance').innerHTML = sage_distance;
    document.getElementById('barh_distance').innerHTML = barh_distance;
    document.getElementById('blitman_distance').innerHTML = blitman_distance;
}




