'use strict';

var View1Ctrl = angular.module('DBApp.view1', ['ngRoute']);

View1Ctrl.controller('View1Ctrl', ['$scope', function($scope) {
  console.log("hello view 1");
  $scope.test = "kjsdfgjksfdgkjksfgjj";
}]);