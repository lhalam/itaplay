
function AllCompanyController($scope, $http, $location) {

  $scope.init = function(){

    $http.get("company/company_view/").then(function (response) {
      $scope.companies = response.data;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });
    $scope.delete = function(company){
        $http.delete("company/delete_company/"+company.pk, {"company_id": company.pk}).then(function (company) {
          $location.path('/#/company');
        }); 
     };      
  };
};

function CompanyAddController($scope, $http,  $location) {
  $scope.init = function(){
    $scope.save = function (company){
      $http.post("company/company_view/", company).success(function (company) {
        $location.path('/#/company');
      });
    };        
  };
};

function CompanyController($scope, $http, $routeParams, $location) {
  var id = $routeParams.company_id;
  $scope.init = function(){
    $http.get("company/current_company_view/"+id).then(function (response) {
      $scope.company = response.data.company;
    }, function(response) {
          console.log(response);
          $scope.data = "Something went wrong";
      });
      $scope.deleteCurrent = function(company){
        $http.delete("company/delete_company/"+id, {"company_id":id}).then(function (company) {
          $location.path('/#/company');
        });
      };      
      $scope.update = function(company){
        $http.post("company/company_view/", company).success(function (company) {
          $location.path('/#/company');
        });
      };    
  };
};

