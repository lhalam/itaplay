'use strict';
var monitorApp = angular.module('monitorApp', ['ngRoute', 'ngMaterial', 'ngMessages', 'ngAnimate']);

monitorApp.config(function($routeProvider) {
    $routeProvider
        .when('/mac=:mac/', {
            templateUrl: '../../../static/js/app/monitor/views/monitor.html',
            controller: MonitorController
        });
      });
