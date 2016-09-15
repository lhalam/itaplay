'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngFileUpload', 'ngMessages', 'LogoutController']);


itaplay.config(function($routeProvider) {
    $routeProvider
       .when('/users', {
            templateUrl: '../../../static/js/app/main/views/users.html',
        })
        .when('/allclips', {
            templateUrl: '../../../static/js/app/clips/views/allclips.html',
            controller: 'AllClipController'
        })
        .when('/projects', {
            templateUrl: '../../../static/js/app/projects/views/all_projects.html',
            controller: 'ProjectCtrl'
        })

        .when('/projects/id=:project_id/', {
            templateUrl: '../../../static/js/app/projects/views/edit_project.html',
            controller: 'EditProjectCtrl'
        })

        .when('/projects/new/', {
            templateUrl: '../../../static/js/app/projects/views/add_project.html',
            controller: 'AddProjectCtrl'
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
       
        .when('/player/', {
            templateUrl: '../../../static/js/app/player/views/all_player.html',
            controller: AllPlayerController
        })
        .when('/player/add_new/', {
            templateUrl: '../../../static/js/app/player/views/add_players.html',
            controller: PlayerAddController          
        })
        

        .when('/player/id=:id/', {
            templateUrl: '../../../static/js/app/player/views/player.html',
            controller: PlayerController          
        })


        .when('/projects/add_project_template/id=:project_id/', {
            templateUrl: '../../../static/js/app/projects/views/add_project_template.html',
            controller: AddProjectTemplateController
        })
    

        .when('/templates', {
            templateUrl: '../../../static/js/app/templates/views/templates.html',
            controller: TemplatesListController
        })

        .when('/templates-add', {
            templateUrl: '../../../static/js/app/templates/views/templates_add.html',
            controller: AddTemplateController
        })


        .when('/template/id=:template_id', {
            templateUrl: '../../../static/js/app/templates/views/current_template.html',
            controller: CurrentTemplateController
        })

        .when('/player/', {
            templateUrl: '../../../static/js/app/player/views/all_player.html',
            controller: AllPlayerController
        })

        .when('/player/add_new/', {
            templateUrl: '../../../static/js/app/player/views/add_players.html',
            controller: PlayerAddController
        })

        .when('/player/id=:id/', {
            templateUrl: '../../../static/js/app/player/views/player.html',
            controller: PlayerController
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
      .accentPalette('blue')
})

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);