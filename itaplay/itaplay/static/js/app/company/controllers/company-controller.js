
function AllCompanyController ($scope, $http, $location, $mdDialog, $cookies) {

    $scope.init = function () {
        $scope.is_superuser = $cookies.get('role') == "True";
        $http.get("company/company_list_view/").then(function (response) {
            $scope.companies = response.data;
        }, function (response) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title(response.data)
                    .ok('Ok')
            );
        });
    };

    $scope.delete = function (company) {
        $http.delete("company/company_details_view/" + company.id, {"company_id": company.id}).then(function (response) {
            $location.path('/company');
        }, function (response) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title(response.data)
                    .ok('Ok')
            );
        });
    };

};


function CompanyAddController ($scope, $http, $location, $mdDialog, $cookies) {
    $scope.init = function () {
        if ($cookies.get('role') == "False"){
            $location.path('/company/');   
        };
        $scope.save = function (company) {
            $http.post("company/company_list_view/", company).then(function (company) {
                $location.path('/company');
            }, function (err) {
                $mdDialog.show({
                    template : '<div class="errorList">' + err.data + "</div>",
                    parent: angular.element(document.body),
                    clickOutsideToClose: true,
                });                    
            });
        };
    };
};


function CompanyController ($scope, $http, $routeParams, $location, $mdDialog, $cookies) {
 
    $scope.init = function () {
        $scope.is_superuser = $cookies.get('role') == "True";
        $http.get("company/company_details_view/" + $routeParams.company_id).then(function (response) {
            $scope.company = response.data.company;
            $scope.users = response.data.users;
            response.data.users.forEach(function (admin){
                if (admin.id == response.data.company.administrator){
                    $scope.company.administrator = admin ;
                };                                                      
            });
        }, function (response) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title(response.data)
                    .ok('Ok')
            );
            $location.path('/company/');   
        });
    };

    $scope.deleteCurrent = function (company) {
        $http.delete("company/company_details_view/"+company.id, {"company_id": company.id}).then(function (company) {
            $location.path('/company');
        }, function (response) {
            $mdDialog.show(
                $mdDialog.alert()
                    .clickOutsideToClose(true)
                    .title(response.data)
                    .ok('Ok')
            );
            $location.path('/company');
        });
    };  

    $scope.update = function (company) {
        $http.put("company/company_details_view/" + company.id + "/", company).then(function (company) {
            $location.path('/company');
        }, function (err) {
            $mdDialog.show({  
                template : '<div class="errorList">' + err.data + "</div>",
                parent: angular.element(document.body),
                clickOutsideToClose: true,
            });
        });
    };

};

