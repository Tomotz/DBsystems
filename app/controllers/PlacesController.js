'use strict';

var PlacesController = angular.module('DBApp.PlacesController', ['ngRoute']);

PlacesController.controller('PlacesController', ['$scope', '$rootScope', '$state', 'PlacesService', function($scope, $rootScope, $state, PlacesService) {
    console.log("PlacesController init");
    
    var autocomplete = get_autocomplete('autocomplete_address_inner');

    var get_places = null;
    if ($state.includes("**.home.**")) {
        console.log("PlacesController: getting general");
        get_places = PlacesService.get_places_home;
    } else if ($state.includes("**.bars.**")){
        console.log("PlacesController: getting bars");
        get_places = PlacesService.get_places_bars;
    } else if ($state.includes("**.rests.**")){
        console.log("PlacesController: getting rests");
        get_places = PlacesService.get_places_food;
    }

    var params = {
        lat : $rootScope.my_user.address.location.lat,
        lng : $rootScope.my_user.address.location.lng,
        radius : 3
    };

    var all_places;
    $scope.places = [];
    get_places(params).then(function (data) {
        console.log("PlacesController: got places - ", data);
        all_places = data;
        $scope.places = all_places.slice(0, 10);
        $scope.data_loaded = true;
    });


    $scope.show_more_clicked = function () {
        $scope.places = $scope.places.concat(all_places.slice($scope.places.length, $scope.places.length + 10));
    };

}]);