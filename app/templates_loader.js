
var paths = [
    "partials/login_signup.html",
    "partials/main.html",
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