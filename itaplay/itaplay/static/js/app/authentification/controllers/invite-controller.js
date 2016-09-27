angular.module('inviteApp',['ngMessages','ngMaterial'])
    .controller("InviteCtrl",['$scope', '$http', '$location', '$window', '$mdDialog',
    function ($scope, $http, $location, $window, $mdDialog) {

        $scope.company = undefined;

        $http.get("/company/company_list_view/").then(function (response) {
          $scope.companies = response.data;
         }, function(response) {
              console.log(response);
            $scope.data = "Something went wrong";
        });

        $scope.inviteUser = function() {
            var req = {
                method: 'POST',
                url: $location.$$absUrl,
                data: {
                    email: $scope.inviteInfo.email,
                    id_company: $scope.company.id,
                }
            };
            $http(req).success(function(){
                $window.location.href = '/';
            }).error(function(err){
                $mdDialog.show(
                    $mdDialog.alert()
                        .clickOutsideToClose(true)
                        .title('Error in form')
                        .textContent(err)
                        .ok('Ok')
                );
            });
        };
}]);
