function CurrentClipController($scope, $sce, $http, $routeParams, $location, Upload, $timeout) {

    var id = $routeParams.clip_id;
    $scope.init = function() {
        $http.get("clips/clips/" + id).then(function(response) {
            $scope.data = response.data;
            $scope.urlAmazon = "https://s3-eu-west-1.amazonaws.com/itaplayadviserireland/media/"
            $scope.myVideo = response.data[0].fields.video
            $scope.fullURL = $scope.urlAmazon + $scope.myVideo

            $scope.trustSrc = function(src) {
                return $sce.trustAsResourceUrl(src);
            }

            $scope.clipUrl = {src: $scope.fullURL};

            console.log(response);


        }, function(response) {
            console.log(response);
            $scope.data = "Something went wrong";
        });
        // $scope.deleteCurrent = function(clip) {
        //     $http.delete("clips/delete/" + id, {"clip_id":id}).then(function(clip) {
        //         $location.path('/#/allclips');
        //     });
        // };

        $scope.update = function(clip) {
            $http.post("clips/clips/" + id, {
                "clip_id":id
            }).success(function(clip) {
                console.log(clip);
                $location.path('/#/allclips');
            });
        }

       
    };


};


