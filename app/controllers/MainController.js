'use strict';

var MainController = angular.module('DBApp.MainController', ['ngRoute']);

MainController.controller('MainController', ['$scope', '$state', function($scope, $state) {
    console.log("MainController init");

    $scope.state = $state;
    

}]);