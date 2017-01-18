'use strict';

var MainController = angular.module('DBApp.MainController', ['ngRoute']);

MainController.controller('MainController', ['$scope', '$state', 'PlacesService', function($scope, $state, PlacesService) {
    console.log("MainController init");

    $scope.state = $state;
    

}]);