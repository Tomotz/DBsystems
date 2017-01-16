'use strict';

// Declare app level module which depends on views, and components
var DBApp = angular.module('DBApp', [
    'ngRoute',
    'ui.router',
    'DBApp.view1',
    'DBApp.view2',
    'DBApp.LoginController'
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
        }).state('view1', {
            url: '/view1',
            // templateURL: 'view1.html',
            template: templates[1],
            controller: 'View1Ctrl'
        }).state('view2', {
            url: '/view2',
            // templateURL: '/view2/view2.html',
            template: templates[2],
            controller: 'View2Ctrl'
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
