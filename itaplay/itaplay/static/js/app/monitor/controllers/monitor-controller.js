function MonitorController($scope, $http, $routeParams) {
    var mac = $routeParams.mac;
    $scope.init = function( ) {
    $http.get('get_by_mac/'+ mac).then(function(response){
        $scope.template = response.data.template;
    }, function(response) {
          console.log(response);
          $scope.data = "Something went wrong";});
    };

};