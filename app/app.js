'use strict';

// Declare app level module which depends on views, and components
var DBApp = angular.module('DBApp', [
    'ngRoute',
    'ui.router',
    'DBApp.MainController',
    'DBApp.PlacesController',
    'DBApp.view2',
    'DBApp.LoginController',
    'DBApp.LoginService',
    'DBApp.PlacesService'
]);


DBApp.config(function($stateProvider) {
    console.log("DBApp Running!");

    var templates = get_templates();
    // get_templates_async().then(function(templates) {
    console.log("DBApp: got templates - ", templates);
    return DBApp.$stateProvider = $stateProvider
        .state('landing_page', {
            url: '/',
            template: templates[0],
            controller: 'LoginController'
        }).state('main', {
            url: '/home',
            template: templates[1],
            controller: 'MainController'
        }).state('main.home', {
            url: '/',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.rests', {
            url: '/rests',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.bars', {
            url: '/bars',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.clubs', {
            url: '/clubs',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.shops', {
            url: '/shops',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.hotels', {
            url: '/hotels',
            template: templates[3],
            controller: 'PlacesController'
        });
    
});
