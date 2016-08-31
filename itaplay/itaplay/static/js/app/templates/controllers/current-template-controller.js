function CurrentTemplateController($scope,
    $http, $routeParams, $location) {
    var id = $routeParams.template_id;
    $scope.init = function() {
        $http({
            method: "GET",
            url: '/templates/current/' + id
        }).then(function mySuccess(response) {
            $scope.data = response.data;
        }, function myError(response) {});
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
