'use strict';

var View1Ctrl = angular.module('DBApp.LoginController', ['ngRoute']);

View1Ctrl.controller('LoginController', ['$scope', '$state', '$rootScope', 'LoginService', function($scope, $state, $rootScope, LoginService) {
    console.log("hello LoginController");
    $scope.show_signup_form = false;

    var defaultBounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(33.5174, 35.9660),
      new google.maps.LatLng(29.6344, 33.5599));

    var addr_input = document.getElementById('autocomplete_address');
    var options = {
      bounds: defaultBounds,
    };

    var autocomplete = new google.maps.places.Autocomplete(addr_input, options);

    $scope.submit_login = function (username) {
        console.log(username);
        LoginService.user_login(username).then(function(user) {
            if (user){
                console.log(user);
                $rootScope.my_user = user;
                $state.go("main.home");
            } else{
                $scope.show_signup_form = true;
            }
        });
    };

    $scope.submit_signup = function () {
        var address = autocomplete.getPlace();
        address.lat = address.geometry.location.lat();
        address.lng = address.geometry.location.lng();
        var user_details = {
            "user_name"  : $scope.username,
            "first_name" : $scope.first_name,
            "last_name"  : $scope.last_name,
            "address"    : address
        };
        console.log("HOLA! ", user_details);
        LoginService.user_signup(user_details).then(function(user) {
            if (user){
                console.log("User signed up, going to main view");
                $rootScope.my_user = user;
                $state.go("main.home");
            }
        });
    }
}]);