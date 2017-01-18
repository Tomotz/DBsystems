'use strict';

var PlacesController = angular.module('DBApp.PlacesController', ['ngRoute']);

PlacesController.controller('PlacesController', ['$scope', '$rootScope', '$state', 'PlacesService', function($scope, $rootScope, $state, PlacesService) {
    console.log("PlacesController init");

    var autocomplete = get_autocomplete('autocomplete_address_inner');

    $scope.selected_radius = 1;
    
    // init tab-related vars 
    var get_places = null;
    if ($state.includes("**.home.**")) {
        console.log("PlacesController: getting general");
        get_places = PlacesService.get_places_home;
        $scope.tab_class = "home_tab";
        $scope.selected_radius = 3;
    } else if ($state.includes("**.rests.**")){
        console.log("PlacesController: getting rests");
        get_places = PlacesService.get_places_food;
        $scope.tab_class = "eat_tab";
    } else if ($state.includes("**.bars.**")){
        console.log("PlacesController: getting bars");
        get_places = PlacesService.get_places_bars;
        $scope.tab_class = "drink_tab";
    } else if ($state.includes("**.clubs.**")){
        console.log("PlacesController: getting clubs");
        get_places = PlacesService.get_places_clubs;
        $scope.tab_class = "dance_tab";
    } else if ($state.includes("**.hotels.**")){
        console.log("PlacesController: getting hotels");
        get_places = PlacesService.get_places_hotels;
        $scope.tab_class = "sleep_tab";
    }

    var params = {
        lat : $rootScope.my_user.address.location.lat,
        lng : $rootScope.my_user.address.location.lng,
        radius : $scope.selected_radius
    };

    var all_places;
    $scope.places = [];
    get_places(params).then(function (data) {
        console.log("PlacesController: got places - ", data);
        all_places = data;
        $scope.places = all_places.slice(0, 10);
        $scope.data_loaded = true;
    });

    // event listener for address changes
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        var new_addr = autocomplete.getPlace();
        params = {
            lat : new_addr.geometry.location.lat(),
            lng : new_addr.geometry.location.lng(),
            radius : $scope.selected_radius
        };
        $scope.data_loaded = false;
        get_places(params).then(function (data) {
            console.log("PlacesController: got places - ", data);
            all_places = data;
            $scope.places = all_places.slice(0, 10);
            $scope.data_loaded = true;
        });
    });

    $scope.show_more_clicked = function () {
        $scope.places = $scope.places.concat(all_places.slice($scope.places.length, $scope.places.length + 10));
    };

}]);