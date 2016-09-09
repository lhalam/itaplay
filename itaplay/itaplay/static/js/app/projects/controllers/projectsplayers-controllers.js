function DialogController ($scope, $http, $location, $mdDialog, parent) {
  $scope.parent = parent;
  $scope.init = function(){
    $http.get("player/player_view/").then(function (response) {
      $scope.players = response.data;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });
  };
  $scope.cancel = function () {
    $mdDialog.cancel();
  };
  $scope.answer = function (answer) {
    $mdDialog.hide(answer);
  };  
};

