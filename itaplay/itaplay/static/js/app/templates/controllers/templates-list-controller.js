function TemplatesListController($scope, $http) {

    $scope.init = function() {
        $http({
            method: "GET",
            url: '/templates/all/'
        }).then(function success(response) {
            $scope.data = response.data;
        }, function error(response) {});
    };

    $scope.delete = function(object) {
        $http({
            method: "DELETE",
            url: '/templates/delete/' + object.id
        }).then(function success(response) {
            var index = $scope.data.indexOf(object)
            $scope.data.splice(index, 1);
            console.debug(response.data)
        }, function error(response) {});
    };
};
