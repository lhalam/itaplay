// function AllUsersController($scope, $http) {

//   $scope.init = function(){
//  };
//     $http.get("/users/all/").then(function (response) {
//       $scope.users = response.data});
//     //  }, function(response) {
//     //     $scope.data = "Something went wrong";
//     // });
 
  
// };

function AllUsersController($scope, $http) {
    $scope.init = function() {
        var api_url = '/users/all/';
        $http.get(api_url)
            .then(function(response) {
                $scope.users = response.data;
                console.log($scope.users);
            });
    };
}
