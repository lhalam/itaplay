itaplay.controller('AllClipController', function($scope, $http) {


    var api_url = '/clips/clips/';
    $http.get(api_url)
        .then(function(response) {
            $scope.data = response.data;
        });



    $scope.delete = function(object) {

        $http({
            url: '/clips/delete/' + object.pk,
            method: 'DELETE',
            data: {
                pk: object.pk
            },
            headers: {
                "Content-Type": "application/json"
            }
        }).then(function(res) {
            var index = $scope.data.indexOf(object)
            $scope.data.splice(index, 1);
            //$scope.data.splice(object,1);
            console.log(res.data);
        }, function(error) {
            console.log(error);
        });
    };


});