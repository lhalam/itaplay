itaplay.controller('TemplatesListController',  function($scope, $http){
  var api_url = '/templates/all/';
  $http.get(api_url)
    .then(function(response){
      $scope.data = response.data;
    });
});