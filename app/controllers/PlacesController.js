'use strict';

var PlacesController = angular.module('DBApp.PlacesController', ['ngRoute']);

PlacesController.controller('PlacesController', ['$scope', '$rootScope', '$state', '$timeout', 'PlacesService', 'LoginService', function($scope, $rootScope, $state, $timeout, PlacesService, LoginService) {
    console.log("PlacesController init");

    // Controller Init
    // ===============
    var autocomplete = get_autocomplete('autocomplete_address_inner');
    var all_places;
    var params;

    // event listener for address changes
    google.maps.event.addListener(autocomplete, 'place_changed', function () {
        var new_addr = autocomplete.getPlace();
        new_addr.lat = new_addr.geometry.location.lat();
        new_addr.lng = new_addr.geometry.location.lng();
        var params = {
            lat : new_addr.lat,
            lng : new_addr.lng,
            radius : $scope.selected_radius
        };
        $scope.data_loaded = false;
        get_places(params).then(function (data) {
            console.log("PlacesController: got places - ", data);
            all_places = data;
            $scope.places = all_places.slice(0, 10);
            $timeout(function () {$scope.data_loaded = true;}, 200);

            // update user address, no need to wait for response
            var user_details = {
                "user_name"  : $scope.my_user.username,
                "first_name" : $scope.my_user.first_name,
                "last_name"  : $scope.my_user.last_name,
                "address"    : new_addr,
                "is_update"  : true
            };
            LoginService.user_signup(user_details);
        });

    });

    // init tab-related vars
    var get_places = null;
    if ($state.includes("**.home.**")) {
        console.log("PlacesController: getting general");
        get_places = PlacesService.get_places_home;
        $scope.tab_class = "home_tab";
        $scope.selected_radius = 5;
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
    } else if ($state.includes("**.shops.**")){
        console.log("PlacesController: getting shops");
        get_places = PlacesService.get_places_shops;
        $scope.tab_class = "shops_tab";
    } else if ($state.includes("**.hotels.**")){
        console.log("PlacesController: getting hotels");
        get_places = PlacesService.get_places_hotels;
        $scope.tab_class = "sleep_tab";
    }

    LoginService.get_my_user().then(function (data) {
        // default radius
        $scope.selected_radius = 2;

        params = {
            lat: $rootScope.my_user.address.location.lat,
            lng: $rootScope.my_user.address.location.lng,
            radius: $scope.selected_radius
        };

        $scope.show_list = true;
        $scope.places = [];
        $scope.refresh_places();
    });


    // Controller Functions
    // ====================
    $scope.refresh_places = function () {
        params.radius = $scope.selected_radius;
        $scope.data_loaded = false;
        get_places(params).then(function (data) {
            console.log("PlacesController: got places - ", data);
            all_places = data;
            $scope.places = all_places.slice(0, 10);
            $scope.all_places_len = all_places.length;
            $timeout(function () {$scope.data_loaded = true;}, 200);
        });
    };

    $scope.show_more_clicked = function () {
        $scope.places = $scope.places.concat(all_places.slice($scope.places.length, $scope.places.length + 10));
    };

    $scope.open_place = function (place) {
        console.log("OPENING ", place);
        PlacesService.get_place_data(place.google_id).then(function (data) {
            if (data){
                console.log("PlacesController: got place details - ", data);
                $scope.place_to_show = data;
                $scope.show_list = false;
            }
        })
    };

    $scope.feeling_lucky_clicked = function () {
        console.log("feeling_lucky_clicked ");
        PlacesService.get_good_avg_rating_places().then(function (data) {
            if (data) {
                console.log("PlacesController: got feeling lucky places - ", data);
                all_places = data;
                $scope.places = all_places.slice(0, 10);
                $timeout(function () {$scope.data_loaded = true;}, 200);
            }
        })
    };

    $scope.get_photogenic_places_clicked = function () {
        console.log("get_photografic_places (hardcoded 30 pics)");
        params = {
            lat: $rootScope.my_user.address.location.lat,
            lng: $rootScope.my_user.address.location.lng,
            num_of_pics: 10
        };
        PlacesService.get_photogenic_places(params).then(function (data) {
            if (data) {
                console.log("PlacesController: got photogenic places - ", data);
                all_places = data;
                $scope.places = all_places.slice(0, 10);
                $timeout(function () {$scope.data_loaded = true;}, 200);
            }
        })
    };

    $scope.search_review = function () {
        console.log("search_review text - ", $scope.review_text);
        params = {
            "text": $scope.review_text
        };
        PlacesService.get_places_by_review(params).then(function (data) {
            if (data) {
                console.log("PlacesController: got places  - ", data);
                $scope.show_list = false;
            }
        })
    }

}]);