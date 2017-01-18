'use strict';

var View1Ctrl = angular.module('DBApp.LoginController', ['ngRoute']);

View1Ctrl.controller('LoginController', ['$scope', '$state', '$rootScope', 'LoginService', function($scope, $state, $rootScope, LoginService) {
    console.log("hello LoginController");
    $scope.show_signup_form = false;
    
    var autocomplete = get_autocomplete('autocomplete_address');

    $scope.submit_login = function (username) {
        console.log(username);
        $scope.user_name_err = false;
        if (!username){
            $scope.user_name_err = true;
            return;
        }
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
        $scope.user_name_err = false;
        var abort = false;
        if (!$scope.username){
            $scope.user_name_err = true;
            abort = true;
        }
        $scope.first_name_err = false;
        if (!$scope.first_name){
            $scope.first_name_err = true;
            abort = true;
        }
        $scope.last_name_err = false;
        if (!$scope.last_name){
            $scope.last_name_err = true;
            abort = true;
        }
        $scope.addr_err = false;
        if (!autocomplete.getPlace()){
            $scope.addr_err = true;
            abort = true;
        }
        if (!abort){
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
    }
}]);