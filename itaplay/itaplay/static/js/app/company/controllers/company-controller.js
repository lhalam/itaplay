
function AllCompanyController($scope, $http, $location) {

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
    });
  };      
};

function CompanyAddController($scope, $http,  $location) {
  $scope.save = function (company){
    $http.post("company/company_list_view/", company).success(function (company) {
      $location.path('/company');
    });
  };        
};

function CompanyController($scope, $http, $routeParams, $location) {
  var id = $routeParams.company_id;
  $scope.init = function(){
    $http.get("company/company_details_view/"+id).then(function (response) {
      $scope.company = response.data.company;
      $scope.users = response.data.users;
    }, function(response) {
          $location.path('/company');
          console.log(response);
          $scope.data = "Something went wrong";
      });
    };
    $scope.deleteCurrent = function(company){
      $http.delete("company/company_details_view/"+id, {"company_id":id}).then(function (company) {
        $location.path('/company');
      }, function(response) {
          console.log(response);
          $scope.data = response;
          $location.path('/company');
        });
    };      
    $scope.update = function(company){
      $http.put("company/company_details_view/"+id, company).success(function (company) {
        $location.path('/company');
      });
    };    
};

