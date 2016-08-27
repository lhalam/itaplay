function CurrentClipController($scope, $sce, $http, $routeParams, $location, Upload, $timeout) {

    var pk = $routeParams.pk;
    $scope.init = function() {
        $http.get("clips/clips/" + pk).then(function(response) {
            $scope.data = response.data;
            $scope.urlAmazon = "https://s3-eu-west-1.amazonaws.com/itaplayadviserireland/"
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
        $scope.deleteCurrent = function(clip) {
            $http.delete("clips/delete/" + pk, {
                "pk": pk
            }).then(function(clip) {
                $location.path('/#/allclips');
            });
        };

        $scope.update = function(clip) {
            $http.post("clips/clips/" + pk, {
                "pk": pk
            }).success(function(clip) {
                console.log(clip);
                $location.path('/#/allclips');
            });
        }

       
    };


};


