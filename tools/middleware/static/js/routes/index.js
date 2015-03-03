angular.module('COMiddleware').config(
    [
        '$stateProvider',
        '$urlRouterProvider',
        function($stateProvider, $urlRouterProvider) {
            $urlRouterProvider.otherwise('/');
            
            $stateProvider.
                state('/', {
                    url: '/',
                    views: {
                        "main_content":
                            {
                                templateUrl: "/list",
                                controller: 'IndexController',
                            }
                    }
                });
        }
    ]
);