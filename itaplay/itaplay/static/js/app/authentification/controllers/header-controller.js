angular.module('LogoutController',['ngMaterial'])
.controller('LogoutController', function($scope,$http, $window) {

    $scope.init = function() {
    $http.get("/users/profile/").then(function (response) {
      $scope.avatar = response.data.AdviserUser.avatar;
      $scope.user = response.data.User.username;
      console.log($scope.user)
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

