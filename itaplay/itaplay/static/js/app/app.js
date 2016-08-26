'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngFileUpload', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider
    	.when('/users', {
            templateUrl: '../../../static/js/app/main/views/users.html'
        })
        .when('/allclips', {
            templateUrl: '../../../static/js/app/clips/views/allclips.html',
            controller: 'AllClipController'
        })
        .when('/projects', {
            templateUrl: '../../../static/js/app/projects/views/all_projects.html'
        })

        .when('/clip/pk=:pk/', {
            templateUrl: '../../../static/js/app/clips/views/current_clip.html',
            controller: 'CurrentClipController'
        })
        .when('/clips', {
            templateUrl: '../../../static/js/app/clips/views/add_clip.html',
            controller: 'ClipController'

        })

        .when('/company/', {
            templateUrl: '../../../static/js/app/company/views/all_company.html',
            controller: AllCompanyController
        })

        .when('/company/add_new/', {
            templateUrl: '../../../static/js/app/company/views/add_companies.html',
            controller: CompanyAddController
        })

        .when('/company/id=:company_id/', {
            templateUrl: '../../../static/js/app/company/views/company.html',
            controller: CompanyController
        })

        .when('/projects/add_project_template/', {
            templateUrl: '../../../static/js/app/projects/views/add_project_template.html'
        })

        .otherwise({redirectTo: '/users'});
})
.run(function($log) {
    $log.info("Starting up");
});

// choose colors for our theme
itaplay.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue');
});

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
