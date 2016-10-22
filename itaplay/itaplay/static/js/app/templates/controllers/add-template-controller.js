function AddTemplateController($scope, Upload, $timeout, $location) {

    $scope.uploadXml = function(file) {
        file.upload = Upload.upload({
            url: '/templates/add/',
            data: {
                templateName: $scope.templateName,
                file: file
            }
        }).then(function success(response) {
            $location.path('/templates');
        });

        file.upload.then(function(response) {
            $timeout(function() {
                file.result = response.data;
            });
        }, function(response) {
            if (response.status > 0)
                $scope.errorMsg = response.status + ': ' + response.data;
        }, function(evt) {
            file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
        });
    };
};
