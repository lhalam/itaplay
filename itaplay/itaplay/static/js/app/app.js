'use strict';

var itaplay = angular.module('itaplay', ['ngRoute',]);


itaplay.config(function($routeProvider) {
    $routeProvider.
        when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        }).
        when('/login',{
            templateUrl: '../../../static/js/app/test/views/login.html',
            controller: LoginController
        }).
        otherwise({redirectTo: '/login'});
}).
run(function($log) {
    $log.info("Starting up");
    console.log("start");
});
