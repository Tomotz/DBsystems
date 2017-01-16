'use strict';

var View1Ctrl = angular.module('DBApp.LoginController', ['ngRoute']);

View1Ctrl.controller('LoginController', ['$scope', function($scope) {
  console.log("hello LoginController");
  $scope.test = "kjsdfgjksfdgkjksfgjj";
}]);