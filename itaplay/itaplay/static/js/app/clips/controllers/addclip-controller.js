//inject angular file upload directives and services.
itaplay.controller('AddClipController', ['$scope', 'Upload', '$timeout', function($scope, Upload, $timeout) {
    $scope.uploadPic = function(file) {
        file.upload = Upload.upload({
            url: '/clips/add_clip/',
            data: {
                filename: $scope.filename,
                description: $scope.description,
                file: file

            },
        });


        file.upload.then(function(response) {
            $timeout(function() {
                file.result = response.data;
            });
        }, function(response) {
            if (response.status > 0)
                $scope.errorMsg = "Something went wrong. Please, check your form";
            // $scope.errorMsg = response.status + ': ' + response.data;
        }, function(evt) {
            // Math.min is to fix IE which reports 200% sometimes
            file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
        });
    }
}]);
