'use strict';

var LoginService = angular.module('DBApp.LoginService', ['ngRoute']);

LoginService.service('LoginService', ['$http', '$q', function($http, $q) {
    var current_user = {};

    this.user_login = function (username) {
        console.log("LoginService logging in - ", username);
        var deferred = $q.defer();
        $http.get('/users/login/' + username + '/').then(function (result) {
            current_user = result.data;
            deferred.resolve(current_user);
        }, function (result) {
            console.log("no user");
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.user_signup = function (details) {
        console.log("LoginService signing up - ", details);
        var deferred = $q.defer();
        $http.post('/users/signup/', details).then(function (result) {
            current_user = result.data;
            deferred.resolve(current_user);
        }, function (result) {
            console.log("Error in signup! ", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_my_user = function () {
        return current_user;
    };
    
}]);