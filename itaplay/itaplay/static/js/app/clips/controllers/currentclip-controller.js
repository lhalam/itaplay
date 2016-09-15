function CurrentClipController($scope, $sce, $http, $routeParams, $location, Upload, $timeout) {

    var id = $routeParams.clip_id;
    $scope.init = function() {
        $http.get("clips/clips/" + id).then(function(response) {
            $scope.data = response.data;
            $scope.myAmazonUrl = response.data[0].fields.url

            $scope.trustSrc = function(src) {
                return $sce.trustAsResourceUrl(src);
            }

            $scope.clipUrl = { src: $scope.myAmazonUrl };

            console.log(response);


        }, function(response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
    };

    $scope.update = function(clip) {
        $http.post("clips/clips/" + id, {
            "clip_id": id
        }).success(function(clip) {
            console.log(clip);
            $location.path('/#/allclips');
        });
    }

};
