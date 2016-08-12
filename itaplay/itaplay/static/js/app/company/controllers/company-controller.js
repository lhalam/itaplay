
function AllCompanyController($scope, $http) {

  $scope.init = function(){

	  $http.get("company/company_view/").then(function (response) {
	    $scope.companies = response.data;
	  }, function(response) {

	 	    console.log(response);
	      $scope.data = "Something went wrong";
	  });
    $scope.delete = function(company){
      $http.delete("company/delete_company/"+company.pk+"/");
    };      
  };
};

function CompanyAddController($scope, $http) {
  $scope.initadd = function(){
    $scope.save = function (company, newCompanyForm){
      $http.post("company/company_view/", company);
    };        
  };
};

function CompanyController($scope, $http, $routeParams) {
  var id = $routeParams.id;
   $scope.initcomp = function(){
        $http.get("company/current_company_view/"+id+"/").then(function (response) {
          $scope.company = response.data.company;
       }, function(response) {
           console.log(response);
          $scope.data = "Something went wrong";
      });
         $scope.delete_current = function(company){
      $http.delete("company/delete_company/"+id+"/");
    };      
       $scope.update = function(company){
      $http.post("company/company_view/", company);
    };      
  };
};
