itaplay.controller('CurrentClipController', function($scope, $http, $routeParams, $location, Upload, $timeout) {

    var pk = $routeParams.pk;
    $scope.init = function() {
        $http.get("clips/clips/" + pk).then(function(response) {
            $scope.data = response.data;
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


});
