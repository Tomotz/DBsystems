'use strict';

// Declare app level module which depends on views, and components
var DBApp = angular.module('DBApp', [
  'ngRoute',
  'ui.router',
  'DBApp.view1',
  'DBApp.view2'
]);


DBApp.config(function($stateProvider) {

    var templates = get_templates();
    
    DBApp.$stateProvider = $stateProvider
        .state('view1', {
            url: '/view1',
            // templateURL: 'view1.html',
            template: templates[0],
            controller: 'View1Ctrl'
        }).state('view2', {
            url: '/view2',
            // templateURL: '/view2/view2.html',
            template: templates[1],
            controller: 'View2Ctrl'
        })
});