'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider
    	.when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })

        .when('/test1', {
            templateUrl: '../../../static/js/app/test/views/test1.html'
        })

        .when('/clips', {
            templateUrl: '../../../static/js/app/test/views/clips.html'
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

itaplay.controller("RegisterCtrl",['$scope', '$http', '$location', '$window', '$mdDialog',
    function ($scope, $http, $location, $window, $mdDialog) {

    $scope.registerUser = function() {
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
        $http(req).success(function(){
            $window.location.href = '/';
        }).error(function(err){
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title('Error in form')
                    .textContent(err)
                    .ok('Ok')
            );
        });
    };
}]);

itaplay.controller("InviteCtrl",['$scope', '$http', '$location', '$window', '$mdDialog',
    function ($scope, $http, $location, $window, $mdDialog) {

    $scope.inviteUser = function() {
        var req = {
            method: 'POST',
            url: $location.$$absUrl,    // can cause problems
            data: {
                email: $scope.inviteInfo.email,
                id_company: $scope.inviteInfo.id_company
            }
        };
        $http(req).success(function(){
            $window.location.href = '/';
        }).error(function(err){
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title('Error in form')
                    .textContent(err)
                    .ok('Ok')
            );
        });
    };
}]);

itaplay.directive("compareTo", function(){
    return {
        require: 'ngModel',
        scope: {
            otherModelValue: "=compareTo"
        },
        link: function (scope, element, attributes, ngModel) {
            ngModel.$validators.compareTo = function (modelValue) {
                return modelValue == scope.otherModelValue;
            };

            scope.$watch("otherModelValue", function () {
                ngModel.$validate();
            })
        }
    }
});
