function CurrentTemplateController($scope,
    $http, $routeParams, $location) {

    $scope.init = function(){
    $scope.pk = $routeParams.pk;
    $http({
        method : "GET",
        url : '/templates/current/' + $scope.pk
    }).then(function mySuccess(response) {
        $scope.data = response.data;
    }, function myError(response) {
        $scope.error_msg = response.statusText;
    });
};

    $scope.deleteCurrent = function () {
        $http({
            method : "DELETE",
            url : '/templates/delete/' + $scope.pk
        }).then(function mySuccess(response) {
            $location.path('/#/templates');
        });
    };
};
