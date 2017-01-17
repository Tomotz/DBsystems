'use strict';

var View1Ctrl = angular.module('DBApp.LoginController', ['ngRoute']);

View1Ctrl.controller('LoginController', ['$scope', '$state', 'LoginService', function($scope, $state, LoginService) {
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
        LoginService.user_login(username).then(function(result) {
            console.log(result);
            
        });
        // var res = LoginService.user_login(username);
        // if (res){
        // //     $state.go("main");
        // // } else {
        //     $scope.show_signup_form = true;
        // }
    };

    $scope.submit_signup = function () {
        var user_details = {
          "first_name" : $scope.first_name,
          "last_name"  : $scope.last_name,
          "address"    : autocomplete.getPlace(),
        };
        console.log("HOLA! ", user_details);
        var res = LoginService.user_signup(user_details);
        if (res){
            $state.go("main");
        } else {
            console.log("ERROR during user signup - ")
        }
    }
}]);