/* LOGIC FOR COOKIES */
function generateUniqueId(length = 10) {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let result = '';
    for (let i = 0; i < length; i++) {
        result += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return result;
}

function getCookie(name) {
    let match = document.cookie.match('^|; ?' + name + '=([^;]*)(;|$)');
    return match ? match[2] : null;
}

window.onload = function() {
    // Check if the 'user_id' cookie already exists
    if (!getCookie('user_id')) {
        // If it doesn't exist, generate a new user_id and set it as a cookie
        let user_id = generateUniqueId();
        document.cookie = "user_id=" + user_id + "; path=/;";
    } else {
        console.log("User ID cookie already set:", getCookie('user_id'))
    }
}