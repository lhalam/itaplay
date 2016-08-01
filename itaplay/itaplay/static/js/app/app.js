'use strict';

var itaplay = angular.module('itaplay', ['ngRoute',]);


itaplay.config(function($routeProvider) {
    $routeProvider.
        when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        }).
        otherwise({redirectTo: '/test'});
}).
run(function($log) {
    $log.info("Starting up");
});
