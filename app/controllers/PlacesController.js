'use strict';

var PlacesController = angular.module('DBApp.PlacesController', ['ngRoute']);

PlacesController.controller('PlacesController', ['$scope', '$rootScope', '$state', 'PlacesService', function($scope, $rootScope, $state, PlacesService) {
    console.log("PlacesController init");

    // var params = {
    //     lat : $rootScope.my_user.address.lat,
    //
    // };

    var get_places = null;
    if ($state.includes("**.home.**")) {
        console.log("PlacesController: getting bars");
        get_places = PlacesService.get_places_home;
    } else if ($state.includes("**.bars.**")){
        console.log("PlacesController: getting bars");
        get_places = PlacesService.get_places_bars;
    } else if ($state.includes("**.rests.**")){
        console.log("PlacesController: getting rests");
        get_places = PlacesService.get_places_food;
    }

}]);