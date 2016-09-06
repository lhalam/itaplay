function AddProjectPlayersController($scope, $http, $location,  $mdDialog) {

   $scope.addPlayers = function ($event){
       $mdDialog.show({
      controller: DialogController,
      templateUrl:"static/js/app/projects/views/add_players.html",
      parent: angular.element(document.body),
      locals: {parent: $scope},
      targetEvent: $event,
      clickOutsideToClose:true,
    
    })
        .then(function (answer) {
                $scope.players = answer;
                console.log($scope.players);
        }, function() {
          $scope.status = 'You cancelled the dialog.';
        });
   };     
  $scope.create = function (project, players){
    data = {
              "project" : project,
              "players" : players
           }
    $http.post("projects/post_project/", data).success(function (data) {
      $location.path('/projects');
    });
  };
};

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

