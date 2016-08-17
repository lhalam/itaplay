'use strict';

var itaplay = angular.module('itaplay', ['ngRoute','ngMaterial', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider
        .when('/test/', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
        })
        .otherwise({redirectTo: '/test'})

        .when('/company/', {
            templateUrl: '../../../static/js/app/company/views/all_company.html',
            controller: AllCompanyController
        })
        .otherwise({redirectTo: '/test'})
       
        .when('/player/', {
            templateUrl: '../../../static/js/app/player/views/all_player.html',
            controller: AllPlayerController
        })
        .otherwise({redirectTo: '/test'})

        .when('/company/add_new/', {
            templateUrl: '../../../static/js/app/company/views/add_companies.html',
            controller: CompanyAddController          
        })
        .otherwise({redirectTo: '/company/'})

        .when('/player/add_new/', {
            templateUrl: '../../../static/js/app/player/views/add_players.html',
            controller: PlayerAddController          
        })
        .otherwise({redirectTo: '/player/'})
       
        .when('/company/id=:id/', {
            templateUrl: '../../../static/js/app/company/views/company.html',
            controller: CompanyController          
        })
        .otherwise({redirectTo: '/company/'})

        .when('/player/id=:id/', {
            templateUrl: '../../../static/js/app/player/views/player.html',
            controller: PlayerController          
        })
        .otherwise({redirectTo: '/player/'})
})

.run(function($log) {
    $log.info("Starting up");
})
// choose colors for our theme
.config(function($mdThemingProvider) {
    $mdThemingProvider.theme('default')
      .primaryPalette('teal')
      .accentPalette('blue')
})

.config(function($httpProvider){
$httpProvider.defaults.xsrfCookieName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

