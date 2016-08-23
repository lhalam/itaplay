itaplay.controller('CurrentTemplateController', function ($scope,
    $http, $routeParams, $location) {


    var pk = $routeParams.pk;
    $http({
        method : "GET",
        url : '/templates/current/' + pk
    }).then(function mySucces(response) {
        $scope.data = response.data;
    }, function myError(response) {
        $scope.data = response.statusText;
    });

    $scope.deleteCurrent = function () {
        $http({
            method : "DELETE",
            url : '/templates/delete/' + pk
        }).then(function mySucces(response) {
            $location.path('/#/templates');
        });
    };
});
