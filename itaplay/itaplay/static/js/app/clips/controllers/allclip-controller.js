itaplay.controller('AllClipController', function($scope, $http) {
  $http.get('/clips/clips/')
  .then(function(response) {
      $scope.data = response.data;
  });
});