'use strict';

var itaplay = angular.module('itaplay', ['ngRoute', 'ngMaterial', 'ngFileUpload', 'ngMessages']);


itaplay.config(function($routeProvider) {
    $routeProvider
<<<<<<< HEAD
        .when('/test/', {
            templateUrl: '../../../static/js/app/test/views/test.html',
            controller: TestController
=======
    	.when('/users', {
            templateUrl: '../../../static/js/app/main/views/users.html'
        })
        .when('/allclips', {
            templateUrl: '../../../static/js/app/clips/views/allclips.html',
            controller: 'AllClipController'
        })
        .when('/projects', {
            templateUrl: '../../../static/js/app/main/views/projects.html'
        })

        .when('/clip/pk=:pk/', {
            templateUrl: '../../../static/js/app/clips/views/current_clip.html',
            controller: 'CurrentClipController'
        })
        .when('/clips', {
            templateUrl: '../../../static/js/app/clips/views/add_clip.html',
            controller: 'ClipController'

>>>>>>> 1cce726579a59faee117fec3c6e7832d60cb0d6b
        })

        .when('/company/', {
            templateUrl: '../../../static/js/app/company/views/all_company.html',
            controller: AllCompanyController
        })
<<<<<<< HEAD
        .otherwise({redirectTo: '/test'})
       
        .when('/player/', {
            templateUrl: '../../../static/js/app/player/views/all_player.html',
            controller: AllPlayerController
        })
        .otherwise({redirectTo: '/test'})
=======
>>>>>>> 1cce726579a59faee117fec3c6e7832d60cb0d6b

        .when('/company/add_new/', {
            templateUrl: '../../../static/js/app/company/views/add_companies.html',
            controller: CompanyAddController
        })
<<<<<<< HEAD
        .otherwise({redirectTo: '/company/'})

        .when('/player/add_new/', {
            templateUrl: '../../../static/js/app/player/views/add_players.html',
            controller: PlayerAddController          
        })
        .otherwise({redirectTo: '/player/'})
       
        .when('/company/id=:id/', {
=======

        .when('/company/id=:company_id/', {
>>>>>>> 1cce726579a59faee117fec3c6e7832d60cb0d6b
            templateUrl: '../../../static/js/app/company/views/company.html',
            controller: CompanyController
        })
<<<<<<< HEAD
        .otherwise({redirectTo: '/company/'})

        .when('/player/id=:id/', {
            templateUrl: '../../../static/js/app/player/views/player.html',
            controller: PlayerController          
        })
        .otherwise({redirectTo: '/player/'})
})
=======
>>>>>>> 1cce726579a59faee117fec3c6e7832d60cb0d6b

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
<<<<<<< HEAD
      .accentPalette('blue')
})

.config(function($httpProvider){
$httpProvider.defaults.xsrfCookieName = 'csrftoken';
$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

=======
      .accentPalette('blue');
});

itaplay.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);
>>>>>>> 1cce726579a59faee117fec3c6e7832d60cb0d6b
