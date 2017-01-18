'use strict';

// Declare app level module which depends on views, and components
var DBApp = angular.module('DBApp', [
    'ngRoute',
    'ui.router',
    'DBApp.PlacesController',
    'DBApp.view2',
    'DBApp.LoginController',
    'DBApp.LoginService',
    'DBApp.PlacesService'
]);


DBApp.config(function($stateProvider) {
    console.log("DBApp Running!");
    var templates = get_templates();

    console.log("DBApp: got templates - ", templates);
    return DBApp.$stateProvider = $stateProvider
        .state('landing_page', {
            url: '/',
            template: templates[0],
            controller: 'LoginController'
        }).state('main', {
            url: '/home',
            template: templates[1],
            // controller: 'MainController'
        }).state('main.home', {
            url: '/',
            template: templates[2],
            // controller: 'MainController'
        }).state('main.bars', {
            url: '/bars',
            // templateURL: 'view1.html',
            template: templates[3],
            controller: 'PlacesController'
        }).state('main.rests', {
            url: '/rests',
            // templateURL: '/view2/view2.html',
            template: templates[4],
            controller: 'PlacesController'
        });

    // get_templates_async().then(function(templates) {
    //     console.log("DBApp: got templates - ", templates);
    //     return DBApp.$stateProvider = $stateProvider
    //         .state('view1', {
    //             url: '/view1',
    //             // templateURL: 'view1.html',
    //             template: templates[0],
    //             controller: 'View1Ctrl'
    //         }).state('view2', {
    //             url: '/view2',
    //             // templateURL: '/view2/view2.html',
    //             template: templates[1],
    //             controller: 'View2Ctrl'
    //         })
    // });
});
