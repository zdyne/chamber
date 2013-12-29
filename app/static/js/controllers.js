// Copyright 2013, Patrick J. Franz

var dashboardApp = angular.module('dashboardApp', []);

dashboardApp.controller('DashboardCtrl', function ($scope) {

    $scope.init = function() {
        $scope.temperatureTimeSeries = new Rickshaw.Graph({
            element: document.getElementById('temperatureTimeSeries'),
            width: 970,
            height: 500,
            renderer: 'line',
            series: new Rickshaw.Series([{ name: 'main' }], undefined)});

        $scope.temperatureTimeSeries.render();
    };

    $scope.init();
});
