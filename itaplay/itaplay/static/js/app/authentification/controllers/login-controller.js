angular.module('loginApp',['ngMessages'])
.controller('LoginController', function($scope,$http) {
    $scope.LoginUser=function(user,password,form) {
        console.log($scope);
        $http({
            method: 'POST',
            url: 'auth/login',
            data: {username: user, password: password}
        }).then(function successCallback(response) {},
                function errorCallback(response) {console.log(response);});
    }
});

