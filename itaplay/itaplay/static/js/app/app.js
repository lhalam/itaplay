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

itaplay.controller("RegisterCtrl",['$scope', '$http', '$location', '$window',
    function ($scope, $http, $location, $window) {

    $scope.registerUser = function() {
        console.log("Start registration");

        var req = {
            method: 'POST',
            url: $location.$$absUrl,    // can cause problems
            data: convertJSONtoDjangoFormat({
                first_name: $scope.registrationInfo.firstName,
                last_name: $scope.registrationInfo.lastName,
                password: $scope.registrationInfo.password,
                confirmPassword: $scope.registrationInfo.confirmPassword
            })
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