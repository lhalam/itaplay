function CurrentTemplateController($scope,
    $http, $routeParams, $location) {
    $scope.init = function() {
        $scope.pk = $routeParams.pk;
        $http({
            method: "GET",
            url: '/templates/current/' + $scope.pk
        }).then(function mySuccess(response) {
            $scope.data = response.data;
        }, function myError(response) {
            console.log(response);
            $scope.error_msg = response.statusText;
        });
    };

    $scope.deleteCurrent = function(template) {
        $http({
            method: "DELETE",
            url: '/templates/delete/' + template.id
        }).then(function mySuccess(response) {
            $location.path('/#/templates');
        });
    };
};
