'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngMessages']);

itaplay.config(function($routeProvider) {
    $routeProvider

    	.when('/test', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })

        .when('/test1', {
            templateUrl: '../../../static/js/app/test/views/test1.html'
        })

        .when('/clips', {
            templateUrl: '../../../static/js/app/test/views/clips.html'
        })
        .otherwise({redirectTo: '/test'})

        .when('/company/', {
            templateUrl: '../../../static/js/app/company/views/all_company.html',
            controller: AllCompanyController
        })
       .otherwise({redirectTo: '/test'})
       
       .when('/company/add_new/', {
            templateUrl: '../../../static/js/app/company/views/add_companies.html',
            controller: CompanyAddController          
        })
       .otherwise({redirectTo: '/company/'})
       
       .when('/company/id=:company_id/', {
            templateUrl: '../../../static/js/app/company/views/company.html',
            controller: CompanyController          
        })
       .otherwise({redirectTo: '/company/'});
})
.run(function($log) {
    $log.info("Starting up");
})

// choose colors for our theme
.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue');
});

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
