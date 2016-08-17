
function AllCompanyController($scope, $http, $location) {

  $scope.init = function(){

    $http.get("company/company_view/").then(function (response) {
      $scope.companies = response.data;
     }, function(response) {
          console.log(response);
        $scope.data = "Something went wrong";
    });
    $scope.delete = function(company){
        $http.delete("company/delete_company/"+company.pk, {"pk": company.pk}).then(function (company) {
          $location.path('/#/company');
        },function (company) {
            $location.path('/#/company');
        }); 
     };      
  };
};

function CompanyAddController($scope, $http,  $location) {
  $scope.initadd = function(){
    $scope.save = function (company){
      $http.post("company/company_view/", company).success(function (company) {
        $location.path('/#/company');
      });
    };        
  };
};

function CompanyController($scope, $http, $routeParams,  $location) {
  var id = $routeParams.id;
  $scope.initcomp = function(){
    $http.get("company/current_company_view/"+id).then(function (response) {
      $scope.company = response.data.company;
    }, function(response) {
          console.log(response);
          $scope.data = "Something went wrong";
      });
      $scope.delete_current = function(company){
        $http.delete("company/delete_company/"+id, {"pk":id}).then(function (company) {
          $location.path('/#/company');
        }, function (company) {
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

