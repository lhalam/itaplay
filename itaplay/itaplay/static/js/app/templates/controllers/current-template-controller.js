function CurrentTemplateController($scope,
    $http, $routeParams, $location) {

    $scope.init = function(){
    var pk = $routeParams.pk;
    $http({
        method : "GET",
        url : '/templates/current/' + pk
    }).then(function mySuccess(response) {
        $scope.data = response.data;
    }, function myError(response) {
        $scope.error_msg = response.statusText;
    });
};

    $scope.deleteCurrent = function () {
        $http({
            method : "DELETE",
            url : '/templates/delete/' + pk
        }).then(function mySuccess(response) {
            $location.path('/#/templates');
        });
    };
};
