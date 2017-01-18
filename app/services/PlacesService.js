'use strict';

var PlacesService = angular.module('DBApp.PlacesService', ['ngRoute']);

PlacesService.service('PlacesService', ['$http', '$q', function($http, $q) {

    this.get_places_home = function (params) {
        console.log("PlacesService get_places_home params - ", params);
        var deferred = $q.defer();
        $http.post('/places/general/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting general places!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_food = function (params) {
        console.log("PlacesService get_places_food params - ", params);
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
        console.log("PlacesService get_places_bars params - ", params);
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
        console.log("PlacesService get_places_hotels params - ", params);
        var deferred = $q.defer();
        $http.post('/places/hotels/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting hotels!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_clubs = function (params) {
        console.log("PlacesService get_places_clubs params - ", params);
        var deferred = $q.defer();
        $http.post('/places/clubs/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting shops!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_place_data = function (params) {
        console.log("PlacesService get_place_data params - ", params);
        var deferred = $q.defer();
        $http.post('/places/details/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting place data!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

}]);
