'use strict';

var MainController = angular.module('DBApp.MainController', ['ngRoute']);

MainController.controller('MainController', ['$scope', '$state', function($scope, $state) {
    console.log("MainController init");

    // inject to scope
    $scope.state = $state;
    $scope.fix_time = fix_time;
    

}]);