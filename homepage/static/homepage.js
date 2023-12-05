    function getCurrentTime() {
        var date = new Date();
        var options = { timeZone: 'America/New_York', hour12: true };
        var timeString = date.toLocaleTimeString('en-US', options);
        document.getElementById("time").textContent = "Time in Troy NY (EST): " + timeString;
    }

    function getHours() {
        var date = new Date();
        var day = date.getDay();
        if(day == 0) //Sunday
        {
            document.getElementById("commons_hours").textContent = "Hours: 9:00 am - 2:00 pm | 4:30 pm - 10:30 pm";
            document.getElementById("sage_hours").textContent = "Hours: 1:30 pm - 8:00 pm";
            document.getElementById("barh_hours").textContent = "Hours: 11:00 am - 1:00 pm";
            document.getElementById("blitman_hours").textContent = "Hours: 10:30 am - 1:30 pm | 5:00 - 8:00 pm";
        }
        else if(day >= 1 && day <= 4) //Monday - Thursday
        {
            document.getElementById("commons_hours").textContent = "Hours: 7:00 am - 3:30 pm | 4:30 pm - 10:30 pm";
            document.getElementById("sage_hours").textContent = "Hours: 7:00 am - 2:30 pm | 4:00 - 8:00 pm";
            document.getElementById("barh_hours").textContent = "Hours: 7:00 am - 9:30 am | 5:00 - 9:00 pm";
            document.getElementById("blitman_hours").textContent = "Hours: 7:00 am - 9:30 am | 5:00 - 8:00 pm";
        }
        else if(day == 5) //Friday
        {
            document.getElementById("commons_hours").textContent = "Hours: 7:00 am - 3:30 pm | 4:30 pm - 9:00 pm";
            document.getElementById("sage_hours").textContent = "Hours: 7:00 am - 2:30 pm | 4:00 - 8:00 pm";
            document.getElementById("barh_hours").textContent = "Hours: 7:00 am - 9:30 am | 5:00 - 9:00 pm";
            document.getElementById("blitman_hours").textContent = "Hours: 7:00 am - 9:30 am | 5:00 - 8:00 pm";
        }
        else if(day == 6) //Saturday
        {
            document.getElementById("commons_hours").textContent = "Hours: 9:00 am - 2:00 pm | 4:30 pm - 9:00 pm";
            document.getElementById("sage_hours").textContent = "Hours: 1:30 pm - 8:00 pm";
            document.getElementById("barh_hours").textContent = "Hours: 11:00 am - 1:00 pm";
            document.getElementById("blitman_hours").textContent = "Hours: 10:30 am - 1:30 pm | 5:00 - 8:00 pm";
        }
    }
    getCurrentTime();
    getHours();
    setInterval(getCurrentTime, 1000);

    var acc = document.getElementsByClassName("title-overlay");
    var i;

    for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        } else {
        panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
    }

    function scrollToTop() {
      window.scrollTo({
        top: 0,
        behavior: 'smooth' 
      });
    }

    function updateDiningHallStatuses() {
        var now = new Date();
        var day = now.getDay(); // 0 is Sunday, 1 is Monday, etc.
        var currentTime = now.getHours() * 60 + now.getMinutes(); // Time in minutes

        updateStatus("commons", getCommonsHours(day), currentTime);
        updateStatus("sage", getSageHours(day), currentTime);
        updateStatus("barh", getBARHHours(day), currentTime);
        updateStatus("blitman", getBlitmanHours(day), currentTime);
        // Add similar lines for other dining halls
    }

    function updateStatus(diningHallId, openHours, currentTime) {
        var statusText = "Closed";
        for (var i = 0; i < openHours.length; i++) {
            var timeRange = openHours[i];
            if (currentTime >= timeRange.start && currentTime <= timeRange.end) {
                statusText = "Open for " + timeRange.meal;
                break;
            }
        }
        document.getElementById(diningHallId + "_status").textContent = "Status: " + statusText;
    }

    function getCommonsHours(day) {
        var breakfast = { start: 7 * 60, end: 10 * 60, meal: "Breakfast" };
        var continentalBreakfast = { start: 10 * 60, end: 11 * 60, meal: "Continental Breakfast" };
        var lunch = { start: 11 * 60, end: 15.5 * 60, meal: "Lunch" };
        var dinnerWeek = { start: 16.5 * 60, end: 21 * 60, meal: "Dinner" };
        var lateNight = { start: 21 * 60, end: 22.5 * 60, meal: "Late Night" };
        var brunch = { start: 9 * 60, end: 14 * 60, meal: "Brunch" };
        var dinnerWeekend = { start: 16.5 * 60, end: 20 * 60, meal: "Dinner" };

        if (day >= 1 && day <= 5) { // Monday to Friday
            return [breakfast, continentalBreakfast, lunch, dinnerWeek];
        } else if (day == 6 || day == 0) { // Saturday and Sunday
            var hours = [brunch, dinnerWeekend];
            if (day == 0) hours.push(lateNight); // Sunday Late Night
            return hours;
        }
    }

    function getSageHours(day) {
        var breakfast = { start: 7 * 60, end: 10 * 60, meal: "Breakfast" };
        var continentalBreakfast = { start: 10 * 60, end: 11 * 60, meal: "Continental Breakfast" };
        var lunch = { start: 11 * 60, end: 14.5 * 60, meal: "Lunch" }; // Until 2:30 PM
        var dinner = { start: 16 * 60, end: 20 * 60, meal: "Dinner" }; // Until 8:00 PM
        var lateLunchWeekend = { start: 13.5 * 60, end: 16 * 60, meal: "Late Lunch" }; // 1:30 PM to 4:00 PM
    
        if (day >= 1 && day <= 5) { // Monday to Friday
            return [breakfast, continentalBreakfast, lunch, dinner];
        } else { // Saturday and Sunday
            return [lateLunchWeekend, dinner];
        }
    }        

    function getBARHHours(day) {
        var breakfast = { start: 7 * 60, end: 9.5 * 60, meal: "Breakfast" }; // 7:00 AM to 9:30 AM
        var dinnerWeek = { start: 17 * 60, end: 21 * 60, meal: "Dinner" }; // 5:00 PM to 9:00 PM
        var brunchWeekend = { start: 11 * 60, end: 13 * 60, meal: "Brunch" }; // 11:00 AM to 1:00 PM
    
        if (day >= 1 && day <= 5) { // Monday to Friday
            return [breakfast, dinnerWeek];
        } else { // Saturday and Sunday
            return [brunchWeekend];
        }
    }

    function getBlitmanHours(day) {
        var breakfastWeek = { start: 7 * 60, end: 9.5 * 60, meal: "Breakfast" }; // 7:00 AM to 9:30 AM, Monday-Friday
        var brunchWeekend = { start: 10.5 * 60, end: 13.5 * 60, meal: "Brunch" }; // 10:30 AM to 1:30 PM, Saturday-Sunday
        var dinner = { start: 17 * 60, end: 20 * 60, meal: "Dinner" }; // 5:00 PM to 8:00 PM, Monday-Sunday
    
        if (day >= 1 && day <= 5) { // Monday to Friday
            return [breakfastWeek, dinner];
        } else { // Saturday and Sunday
            return [brunchWeekend, dinner];
        }
    }
    
    updateDiningHallStatuses();
    setInterval(updateDiningHallStatuses, 60000); // Update status every minute

