function InviteUserController ($scope, $http, $location, $window, $mdDialog) {

    $scope.company = undefined;

    $scope.init = function() {
        $http.get("/company/company_list_view/")
        .then(function (response) {
            $scope.companies = response.data;
        });
    };

    $scope.inviteUser = function () {
        if ($scope.company == undefined) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title('Error in form')
                    .textContent("You need to select company first!")
                    .ok('Ok')
            );
            return;
        }

        var req = {
            method: 'POST',
            url: '/auth/invite',
            data: {
                email: $scope.inviteInfo.email,
                id_company: $scope.company.id,
            }
        };

        $http(req).success(function () {
            $window.location.href = '#/invitations';
        }).error(function (err) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title('Error in form')
                    .textContent(err)
                    .ok('Ok')
            );
        });
    };
}