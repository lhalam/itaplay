angular.module('inviteApp',['ngMessages','ngMaterial'])
    .controller("InviteCtrl",['$scope', '$http', '$location', '$window', '$mdDialog',
    function ($scope, $http, $location, $window, $mdDialog) {

    $scope.inviteUser = function() {
        var req = {
            method: 'POST',
            url: $location.$$absUrl,    // can cause problems
            data: {
                email: $scope.inviteInfo.email,
                id_company: $scope.inviteInfo.id_company
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
