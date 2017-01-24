'use strict';

var LoginService = angular.module('DBApp.LoginService', ['ngRoute']);

LoginService.service('LoginService', ['$http', '$q', '$rootScope', function($http, $q, $rootScope) {
    var current_user = null;

    this.user_login = function (username) {
        console.log("LoginService logging in - ", username);
        var deferred = $q.defer();
        $http.get('/users/login/' + username + '/').then(function (result) {
            current_user = result.data;
            $rootScope.my_user = current_user;
            window.localStorage.setItem("my_user_name", current_user.username);
            console.log("LoginService logged in - ", current_user);
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
            $rootScope.my_user = current_user;
            window.localStorage.setItem("my_user_name", current_user.username);
            deferred.resolve(current_user);
        }, function (result) {
            console.log("Error in signup! ", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_my_user = function () {
        if (current_user == null && window.localStorage.getItem("my_user_name")){
            return this.user_login(window.localStorage.getItem("my_user_name"));
        }
        $rootScope.my_user = current_user;
        return $q.when(current_user);
    };

}]);
