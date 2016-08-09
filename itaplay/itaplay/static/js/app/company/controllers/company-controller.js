
function AllCompanyController($scope, $http) {

  $scope.init = function(){

	  $http.get("company/company_get/").then(function (response) {
	    $scope.companies = response.data.company;
	  }, function(response) {

	 	    console.log(response);
	      $scope.data = "Something went wrong";
	  });
  };
};

function CompanyAddController($scope, $http) {

  $scope.initadd = function(){

    $scope.save = function (company, newCompanyForm){
      $http.post("company/company_post/", company);
    };        
  };
};
