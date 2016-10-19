function UserController($scope, $http) {
    $scope.init = function() {
        var api_url = '/users/profile/';
        $http.get(api_url)
            .then(function(response) {
                $scope.user = response.data;
            });
   };
    $scope.update = function(user){
    $http.put("/users/profile/", user).then(function (user) {
      $location.path('/profile');
    }, function(response) {
        $mdDialog.show(
            $mdDialog.alert()
            .clickOutsideToClose(true)
            .title(response.data)
            .ok('Ok')
        );
    });
   };
}
