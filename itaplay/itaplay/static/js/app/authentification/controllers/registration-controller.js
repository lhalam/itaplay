registrationModule = angular.module('registerApp',['ngMaterial', 'ngMessages']);

registrationModule.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
        .primaryPalette('teal')
        .accentPalette('blue');
});

registrationModule.controller("RegisterCtrl",['$scope', '$http', '$location', '$window', '$mdDialog',
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

registrationModule.directive("compareTo", function(){
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
