function TemplatesListController($scope, $http){
 
    $scope.init = function(){
    $http({
        method : "GET",
        url : '/templates/all/'
    }).then(function mySucces(response) {
        $scope.data = response.data;
    });
};
    $scope.delete = function (object) {
        $http({
            method : "DELETE",
            url : '/templates/delete/' + object.id
            // data: {
            //     pk: object.pk
            // }
        }).then(function mySucces(response) {
            var index = $scope.data.indexOf(object)
            $scope.data.splice(index, 1);
            console.debug(response.data)
        }, function myError(response) {
            console.log(error);
        });
    }
};
