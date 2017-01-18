
var paths = [
    "partials/login_signup.html",
    "partials/main.html",
    "partials/home.html",
    "partials/view1.html",
    "partials/view2.html"
];

function get_templates_async() {
    var $q = window.angular.injector(['ng']).get('$q');
    var promises = [];
    paths.forEach(function (path) {
        promises.push($.get(path));
    });
    return $q.all(promises);
}

function get_templates() {
    var temp = [];
    paths.forEach(function (path) {
        temp.push($.get(path));
    });
    return temp
}

function get_autocomplete(element_id) {
    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(33.5174, 35.9660),
        new google.maps.LatLng(29.6344, 33.5599));

    var addr_input = document.getElementById(element_id);
    var options = {
        bounds: defaultBounds,
    };

    return new google.maps.places.Autocomplete(addr_input, options);
}