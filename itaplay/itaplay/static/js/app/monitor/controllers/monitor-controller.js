function MonitorController($scope, $http, $routeParams) {
    var mac = $routeParams.mac;
    $scope.init = function( ) {
    $http.get('monitor/get_by_mac/'+ mac).then(function(response){
        $scope.project = response.data;
    }, function(response) {
          console.log(response);
          $scope.data = "Something went wrong";});
    };

};