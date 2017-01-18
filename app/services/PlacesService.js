'use strict';

var PlacesService = angular.module('DBApp.PlacesService', ['ngRoute']);

PlacesService.service('PlacesService', ['$http', '$q', function($http, $q) {

    this.get_places_food = function (params) {
        console.log("PlacesService logging in - ", username);
        var deferred = $q.defer();
        $http.post('/places/food/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting food places!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_bars = function (params) {
        console.log("PlacesService logging in - ", username);
        var deferred = $q.defer();
        $http.post('/places/bars/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting bars!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_hotels = function (params) {
        console.log("PlacesService logging in - ", username);
        var deferred = $q.defer();
        $http.post('/places/hotels/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting hotels!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_shops = function (params) {
        console.log("PlacesService logging in - ", username);
        var deferred = $q.defer();
        $http.post('/places/shops/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting shops!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

}]);
