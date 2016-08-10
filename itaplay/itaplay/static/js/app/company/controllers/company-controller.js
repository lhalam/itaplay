
function AllCompanyController($scope, $http) {

  $scope.init = function(){

	  $http.get("company/company_get/").then(function (response) {
	    $scope.companies = response.data.company;
	  }, function(response) {

	 	    console.log(response);
	      $scope.data = "Something went wrong";
	  });
    $scope.delete = function(company){
      $http.post("company/delete_company/", company);
    };      
  };
};

function CompanyAddController($scope, $http) {
  $scope.initadd = function(){
    $scope.save = function (company, newCompanyForm){
      $http.post("company/company_post/", company);
    };        
  };
};

function CompanyController($scope, $http, $routeParams) {
  var id = $routeParams.id;
   $scope.initcomp = function(){
        $http.get("company/get_current/"+id+"/").then(function (response) {
          $scope.company = response.data.current_company;
       }, function(response) {
           console.log(response);
          $scope.data = "Something went wrong";
      });
         $scope.delete_current = function(company){
      $http.post("company/delete_company/", company);
    };      
       $scope.update = function(company){
      $http.post("company/edit_company/", company);
    };      
  };
};
