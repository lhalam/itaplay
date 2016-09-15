angular.module('LogoutController',['ngMaterial'])
.controller('LogoutController', function($scope,$http, $window) {

    $scope.LogoutUser = function() {
        $http.get('/auth/logout').then(function(response) {
            $window.location.href = '/';
        },
            function errorCallback(response) {
            });
    }
});

//function HeaderController($scope, $http, $location) {
//  $scope.LogoutUser  = function() {
//    console.log("logOutUser");
//      $scope.logOut = function (){
//        console.log("logOut");
//            $http.get('/auth/logout').then(function(response) {
//                $window.location.href = '/';
//            }, function errorCallback(response) {
//            });
//      };
//  }
//};
