angular.module('LogoutController',['ngMaterial'])
.controller('LogoutController', function($scope,$http, $window) {

    $scope.init = function() {
    $http.get("/users/all/").then(function (response) {
      $scope.avatar = response.data.AdviserUser.avatar;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });
  };

    $scope.LogoutUser = function() {
        $http.get('/auth/logout').then(function(response) {
                $window.location.href = '/';
            }, function errorCallback(response) {
            });
  }
});

