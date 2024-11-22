
/* LOGIC FOR CURRENT TIME */

function getCurrentTime() {
    var date = new Date();
    var options = { timeZone: 'America/New_York', hour12: true };
    var timeString = date.toLocaleTimeString('en-US', options);
    document.getElementById("time").textContent = "Time in Troy NY (EST): " + timeString;
}
getCurrentTime();
setInterval(getCurrentTime, 1000);

/* LOGIC FOR CALORIE CALCULATIONS */

let totalCalories = 0

let food_items = []

let dropdown = document.getElementById("dropdown");

function addCalories(calories, item){
    document.getElementById("dropdown").style.display = "block";
    food_items.push([item, calories]);
    
    totalCalories += calories;
    document.getElementById("totalCalories").textContent = totalCalories;
}

function clearCalories(){
    totalCalories = 0
    document.getElementById("totalCalories").textContent = totalCalories;
}


dropdown = document.getElementById("dropdown");

dropdown.addEventListener('click', function() {
    food_items = dropdown.options.length;


    console.log("This is the legnth", food_items);
})






/* LOGIC FOR ACCORDIONS */

document.addEventListener("DOMContentLoaded", function() {
    var acc = document.querySelectorAll(".accordion");

    // Attach event listeners to each accordion
    for (var i = 0; i < acc.length; i++) {

        acc[i].addEventListener("click", function() {

            // Toggle the active class
            this.classList.toggle("active");

            // Get the associated panel (next sibling)
            var panel = this.nextElementSibling;

            if (!panel) return;  // If no panel is found, skip

            // Check whether the panel is open or closed
            var computedMaxHeight = window.getComputedStyle(panel).maxHeight;

            if (computedMaxHeight !== "0px" && computedMaxHeight !== "none") {
                panel.style.maxHeight = "0px"; // Explicitly set max-height to 0 to close
            } else {
                panel.style.maxHeight = panel.scrollHeight + "px"; // Open panel based on scrollHeight
            }

            // Delay the outer panel height adjustment slightly to allow for DOM updates
            setTimeout(() => adjustOuterPanelHeight(this), 350); // Adjust timing to give animation time to finish
        });
    }
});

// Helper function to adjust the outer panel height
function adjustOuterPanelHeight(element) {
    var outerPanel = element.closest('.panel');
    if (outerPanel) {

        // Recalculate the scrollHeight of the outer panel
        outerPanel.style.maxHeight = outerPanel.scrollHeight + "px";
    }
}

// Toggle description expansion and adjust the outer accordion dynamically
function toggleDescription(button) {
    var descriptionDiv = button.parentNode.nextElementSibling;

    if (descriptionDiv.style.display === "none" || 
        descriptionDiv.style.display === "") {
        descriptionDiv.style.display = "block";
        button.textContent = "-";
    } else {
        descriptionDiv.style.display = "none";
        button.textContent = "+";
    }

    // Adjust the heights of all parent panels
    adjustParentPanels(button);
}

function adjustParentPanels(element) {
    var parentPanel = element.closest('.panel');

    if (parentPanel) {
        // Temporarily set max-height to 'none' to get full scrollHeight
        parentPanel.style.maxHeight = 'none';

        // Force reflow to ensure the browser calculates the new height
        parentPanel.offsetHeight;

        // Set the max-height to the new scrollHeight
        parentPanel.style.maxHeight = parentPanel.scrollHeight + "px";

        // Recursively adjust parent panels
        adjustParentPanels(parentPanel.parentNode);
    }
}

/* LOGIC FOR SUBMITTING RATINGS */

$(document).ready(function() {
    $(document).on('click', '.star-rating .star', function() {
        var rating = $(this).data('value');
        var station = $(this).closest('.rating-section').data('station');
        var dining_hall = $(this).closest('.rating-section').data('dining-hall');
        var meal = $(this).closest('.rating-section').data('meal');             // Get meal info from parent div

        // Call the function to submit the rating
        submitRating(rating, station, dining_hall, meal);
    });

    function submitRating(rating, station, dining_hall, meal) {
        fetch('/' + diningHallName + '/submit-rating/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken  // CSRF token from Django
            },
            body: JSON.stringify({ rating: rating, station: station, dining_hall: dining_hall, meal: meal })  // Include rating and station in the body
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response
            alert(data.message);
            if (data.success) {
                updateStarRatings(station, meal, rating);  // Call to update stars
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function updateStarRatings(station, meal, newRating) {
        const starElements = $(`.rating-section[data-station="${station}"][data-meal="${meal}"] .star`);
        
        // Loop through each star and update the class based on the new rating
        starElements.each(function() {
            const starValue = $(this).data('value');
            $(this).toggleClass('selected', starValue <= newRating);
        });
    }
});

/* LOGIC FOR WEBSOCKETS */

const ratingSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/log/' + diningHallName + '/'
);

ratingSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const ratingsArray = data.average_ratings
    ratingsArray.forEach(item => {
        const ratingElement = document.getElementById(`rating-${item.station}-${item.meal}`);
        if (ratingElement) {
            ratingElement.textContent = item.average_rating
        }
    });
};

ratingSocket.onclose = function(e) {
    console.error('Rating socket closed unexpectedly');
};