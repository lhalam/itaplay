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
      .accentPalette('blue');
});

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

itaplay.controller("RegisterCtrl",['$scope', '$http', '$location', '$window',
    function ($scope, $http, $location, $window) {

    $scope.registerUser = function() {
        console.log("Start registration");

        var req = {
            method: 'POST',
            url: $location.$$absUrl,    // can cause problems
            data: {
                first_name: $scope.registrationInfo.firstName,
                last_name: $scope.registrationInfo.lastName,
                password: $scope.registrationInfo.password,
                confirm_password: $scope.registrationInfo.confirmPassword
            }
        };
        console.log(req.data);
        $http(req).success(function(){
            console.log("Successful registration");
            $window.location.href = '/';
        }).error(function(err){
            alert(err);
        });
    };
}]);