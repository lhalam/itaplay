function AllUsersController($scope, $http) {
    $scope.init = function() {
        var api_url = '/users/all/';
        $http.get(api_url)
            .then(function(response) {
                $scope.users = response.data;
                console.log($scope.users);
            });
    };
}
