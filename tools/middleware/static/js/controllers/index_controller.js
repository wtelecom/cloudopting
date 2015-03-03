angular.module('COMiddleware').controller('IndexController',
    [
        '$scope',
        'restService',
        function ($scope, restService) {
            $scope.fields = [];
            restService.get(
                {},
                apiPrefix + '/tosca/configurations',
                function(data, status, headers, config) {
                    if (data[0].fields.length) {
                        $scope.fields = data[0].fields;
                    }
                },
                function(data, status, headers, config) {}
            );
        }
    ]
);