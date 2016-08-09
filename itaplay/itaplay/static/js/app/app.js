'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngMessages']);


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

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';
}]);

itaplay.controller("RegisterCtrl",['$scope', '$http', function ($scope, $http) {
    $scope.registrationInfo = {
        firstName : "John",
        lastName: "Kul",
        password : "password",
        confirmPassword: "password"
    };
    $scope.list = [];
    $scope.firstName = "";
    $scope.registerUser = function() {
        console.log("Start registration");

        var req = {
            method: 'POST',
            url: 'http://127.0.0.1:8000/auth/register?code=1',
            data: convertJSONtoDjangoFormat({
                first_name: $scope.registrationInfo.firstName,
                last_name: $scope.registrationInfo.lastName,
                password: $scope.registrationInfo.password,
                confirmPassword: $scope.registrationInfo.confirmPassword
            })
        };
        console.log(req.data);
        $http(req);

    };
}]);

function convertJSONtoDjangoFormat(data){
    var str = "";
    for (var property in data) {
        if (data.hasOwnProperty(property)) {
            str += property + "=" + data[property];
            str += "&";
        }
    }
    return str
}