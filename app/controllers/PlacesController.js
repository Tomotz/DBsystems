'use strict';

var PlacesController = angular.module('DBApp.PlacesController', ['ngRoute']);

PlacesController.controller('PlacesController', ['$scope', '$state', 'PlacesService', function($scope, $state, PlacesService) {
    console.log("PlacesController init");

    var get_places = null;
    if ($state.includes("**.bars.**")){
        console.log("PlacesController: getting bars");
        get_places = PlacesService.get_places_bars;
    } else if ($state.includes("**.rests.**")){
        console.log("PlacesController: getting rests");
        get_places = PlacesService.get_places_food;
    }

}]);