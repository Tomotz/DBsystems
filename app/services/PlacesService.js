'use strict';

var PlacesService = angular.module('DBApp.PlacesService', ['ngRoute']);

PlacesService.service('PlacesService', ['$rootScope', '$http', '$q', function($rootScope, $http, $q) {

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
            console.log("Error getting clubs!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_shops = function (params) {
        console.log("PlacesService get_places_shops params - ", params);
        var deferred = $q.defer();
        $http.post('/places/shops/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting shops!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_place_data = function (place_id) {
        console.log("PlacesService get_place_data place_id - ", place_id);
        var deferred = $q.defer();
        $http.get('/places/details/' + place_id + '/').then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting place data!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_good_avg_rating_places = function () {
        console.log("PlacesService get_good_avg_rating_places");
        var deferred = $q.defer();
        $http.get('/places/feeling_lucky/' + $rootScope.my_user.address.location.lat + '/' + $rootScope.my_user.address.location.lng + '/').then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting feeling lucky places!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_photogenic_places = function (params) {
        console.log("PlacesService get_photogenic_places - ", params);
        var deferred = $q.defer();
        // $http.get('/places/photogenic/' + num + '/').then(function (result) {
        $http.post('/places/photogenic/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting photogenic places!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

    this.get_places_by_review = function (params) {
        console.log("PlacesService get_places_by_review, search text - ", params);
        var deferred = $q.defer();
        $http.post('/places/review_text/', params).then(function (result) {
            deferred.resolve(result.data);
        }, function (result) {
            console.log("Error getting feeling lucky places!", result);
            deferred.resolve(false);
        });
        return deferred.promise;
    };

}]);
