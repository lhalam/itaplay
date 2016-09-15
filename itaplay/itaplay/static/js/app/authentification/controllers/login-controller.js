angular.module('loginApp',['ngMaterial', 'ngMessages'])
.controller('LoginController', function($scope,$http, $window) {

    $scope.LoginUser = function(user,password,form) {
        $http({
            method: 'POST',
            url: '/auth/login',
            data: {username: user, password: password}
        }).then(function successCallback(response) {
            $window.location.href = '/';
            },
                function errorCallback(response) {
                });
    }

//    $scope.LogoutUser = function() {
//        $http.get('/auth/logout').then(function(response) {
//            $window.location.href = '/';
//        },
//            function errorCallback(response) {
//            });
//    }
});
