'use strict';

// Declare app level module which depends on views, and components
var DBApp = angular.module('DBApp', [
  'ngRoute',
  'ui.router',
  'DBApp.view1',
  'DBApp.view2'
]);


DBApp.config(function($stateProvider) {

  var a = $.get("view1/view1.html");
  DBApp.$stateProvider = $stateProvider
      .state('view1', {
        url: '/view1',
        // templateURL: 'view1.html',
        template: a,
        controller: 'View1Ctrl'
      }).state('view2', {
        url: '/view2',
        templateURL: 'view2/view2.html',
        controller: 'View2Ctrl'
      })
});