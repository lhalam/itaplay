function UserController($scope, $http) {
    $scope.init = function() {
        var api_url = '/users/profile/';
        $http.get(api_url)
            .then(function(response) {
                $scope.users = response.data;
                $scope.user = response.data;
                console.log($scope.user.User.username);
            });
    };
}
