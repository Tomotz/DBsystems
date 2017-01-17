'use strict';

var LoginService = angular.module('DBApp.LoginService', ['ngRoute']);

LoginService.service('LoginService', ['$http', function($http) {
    this.user_login = function (username) {
        console.log("LoginService logging in - ", username);
        return $http.get('/users/login/' + username + '/');
    };

    this.user_signup = function (details) {
        console.log("LoginService signing up - ", details);
        return true;
    };

}]);