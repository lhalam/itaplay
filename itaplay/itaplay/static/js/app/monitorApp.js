'use strict';
var monitorApp = angular.module('monitorApp', ['ngRoute', 'ngMaterial', 'ngMessages']);

monitorApp.config(function($routeProvider) {
    $routeProvider
        .when('/mac=:mac/', {
            templateUrl: '../../../static/js/app/monitor/view/monitor.html',
            controller: MonitorController
        });
      });
