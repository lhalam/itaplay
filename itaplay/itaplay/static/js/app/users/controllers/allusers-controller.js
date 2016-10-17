function AllUsersController($scope, $http, $route) {
    $scope.init = function() {
        var api_url = '/users/all/';
        $http.get(api_url)
            .then(function(response) {
            	$scope.users = response.data;
            });
    };
    $scope.delete = function(user) {
        $http.delete('/users/all/' + user.id + "/")
            .success(function() {
                $route.reload();
            });
    };
}
