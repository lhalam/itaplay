angular.module('loginApp',['ngMaterial', 'ngMessages'])
.controller('LoginController',['$scope', '$http', '$location', '$window', '$mdDialog',
    function($scope, $http, $location, $window, $mdDialog) {

    $scope.LoginUser = function(user, password) {
        $http({
            method: 'POST',
            url: '/auth/login',
            data: {username: user, password: password}
        }).success(function() {
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
    }

}]);
