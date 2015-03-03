/**
 * @file app.js
 * @namespace AngularJS Main App
 * AngularJS needs controllers to operate, this file create the main app.
 */

angular.module(
    'COMiddleware',
    [
        'ui.router',
        'RESTservice',
    ]
);


var apiPrefix = '/api/v1';
