itaplay.controller('AddTemplateController', ['$scope', 'Upload', '$timeout', '$location', 
    function ($scope, Upload, $timeout, $location) {

    $scope.uploadXml = function(file) {
    file.upload = Upload.upload({
        url: '/templates/add/',
        data: {templateName: $scope.templateName
        , file: file
    }}).then(function(template){
        $location.path('/#/templates');
    });

    file.upload.then(function (response) {
        $timeout(function () {
        file.result = response.data;
      });
    }, function (response) {
      if (response.status > 0)
        $scope.errorMsg = response.status + ': ' + response.data;
    }, function (evt) {
      // Math.min is to fix IE which reports 200% sometimes
      file.progress = Math.min(100, parseInt(100.0 * evt.loaded / evt.total));
    });
    }
}]);
