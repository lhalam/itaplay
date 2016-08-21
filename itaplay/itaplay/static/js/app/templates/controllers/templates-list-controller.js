itaplay.controller('TemplatesListController',  function($scope, $http){
    
    var api_url = '/templates/all/';
    $http.get(api_url)
    .then(function(response){
        $scope.data = response.data;
    });

    $scope.delete = function(object) {

        $http({
            url: '/templates/delete/' + object.pk,
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
            console.log(res.data);
        }, function(error) {
            console.log(error);
        });
    };

});
