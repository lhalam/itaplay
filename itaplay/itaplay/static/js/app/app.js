'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider.
        when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })

}).
run(function($log) {
    $log.info("Starting up");
    console.log("start");
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