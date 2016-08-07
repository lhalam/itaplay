'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial']);


itaplay.config(function($routeProvider) {
    $routeProvider
    	.when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })
        .otherwise({redirectTo: '/test'})

        .when('/test1', {
            templateUrl: '../../../static/js/app/test/views/test1.html',
            
        })
        .otherwise({redirectTo: '/test'})

        .when('/clips', {
            templateUrl: '../../../static/js/app/test/views/clips.html',
            
        })
        .otherwise({redirectTo: '/test'});
})
.run(function($log) {
    $log.info("Starting up");
})

// choose colors for our theme
.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue')
      .dark();


});