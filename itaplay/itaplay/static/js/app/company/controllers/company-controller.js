
function AllCompanyController($scope, $http, $location, $mdDialog) {

  $scope.init = function(){

    $http.get("company/company_list_view/").then(function (response) {
      $scope.companies = response.data;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });
  };
  $scope.delete = function(company){
    $http.delete("company/company_details_view/"+company.id, {"company_id": company.id}).then(function (response) {
        $location.path('/company');
      }, function(response) {
          $mdDialog.show(
              $mdDialog.alert()
              .clickOutsideToClose(true)
              .title(response.data)
              .ok('Ok')
          );
    });
  };      
  $scope.addNewCompany = function(){
       $location.path('/company/add_new/');
  };
};

function CompanyAddController($scope, $http, $location, $mdDialog) {
  $scope.save = function (company){
    $http.post("company/company_list_view/", company).then(function (company) {
        $location.path('/company');
      }, function(response) {
          $mdDialog.show(
              $mdDialog.alert()
              .clickOutsideToClose(true)
              .title(response.data)
              .ok('Ok')
            );
          $location.path('/company/add_new/');
      });
    };        
};

function CompanyController($scope, $http, $routeParams, $location, $mdDialog) {
  var id = $routeParams.company_id;
  $scope.init = function(){
    $http.get("company/company_details_view/"+id).then(function (response) {
      $scope.company = response.data.company;
      $scope.users = response.data.users;
    }, function(response) {
        $mdDialog.show(
            $mdDialog.alert()
            .clickOutsideToClose(true)
            .title(response.data)
            .ok('Ok')
        );
        $location.path('/company/');
          
    });
  };
  $scope.deleteCurrent = function(company){
    $http.delete("company/company_details_view/"+id, {"company_id":id}).then(function (company) {
      $location.path('/company');
    }, function(response) {
        $mdDialog.show(
            $mdDialog.alert()
            .clickOutsideToClose(true)
            .title(response.data)
            .ok('Ok')
        );
        $location.path('/company');
    });
  };      
  $scope.update = function(company){
    $http.put("company/company_details_view/"+id +"/", company).then(function (company) {
      $location.path('/company');
    }, function(response) {
        $mdDialog.show(
            $mdDialog.alert()
            .clickOutsideToClose(true)
            .title(response.data)
            .ok('Ok')
        );
        $location.path('/company/id='+id);
    });
  };    
};

