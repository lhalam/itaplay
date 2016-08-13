itaplay.controller('AllClipController', function($scope, $http) {
   
   
  var api_url = '/clips/clips/';
  $http.get(api_url)
  .then(function(response) {
      $scope.data = response.data;
  });

$scope.remove = function(item){ 
     var index = $scope.data.indexOf(item)
     $scope.data.splice(index,1);    
    };

$scope.delete = function(object) {

        $http({ url: '/clips/delete/' + object.pk, 
                method: 'POST', 
                data: {pk: object.pk}, 
                headers: {"Content-Type": "application/json"}
        }).then(function(res) {
            console.log(res.data);
        }, function(error) {
            console.log(error);
        });
    };     
  
});

