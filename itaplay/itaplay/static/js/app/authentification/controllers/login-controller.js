angular.module('loginApp',['ngMessages'])
.controller('LoginController', function($scope,$http, $window) {
    $scope.LoginUser = function(user,password,form) {
        console.log($scope);
        $http({
            method: 'POST',
            url: '/auth/login',
            data: {username: user, password: password}
        }).then(function successCallback(response) {
            $window.location.href = '/';
            },
                function errorCallback(response) {console.log(response);});
    }
});

