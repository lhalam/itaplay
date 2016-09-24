function AllClipController($scope, $http) {
    $scope.init = function() {
        var api_url = '/clips/allclips/';
        $http.get(api_url)
            .then(function(response) {
                $scope.clips = response.data;
                console.log($scope.clips);
            });
    };

    $scope.delete = function(object) {

        $http.delete('/clips/delete/' + object.pk, {pk: object.pk, 
                headers: {"Content-Type": "application/json"}})
        .then(function(res) {
            var index = $scope.clips.indexOf(object);
            $scope.clips.splice(index, 1);
            //$scope.data.splice(object,1);
            console.log(res.clips);
        }, function(error) {
            console.log(error);
        });
    };
};
