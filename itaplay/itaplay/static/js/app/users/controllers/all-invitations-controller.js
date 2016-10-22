function AllInvitationsController($scope, $http) {
    $scope.init = function() {
        var api_url = '/users/invitations/';
        $http.get(api_url)
            .then(function(response) {
                $scope.invitations = response.data;
                console.log($scope.users);
            });
    };
}
