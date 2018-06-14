var app = angular.module("appCiutadaEstelar", ['ngCookies']);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.config(['$httpProvider',
    function(provider) {
        provider.defaults.xsrfCookieName = 'csrftoken';
        provider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

app.controller('NausController', function($scope, $sce, $http) {
    $scope.veureProducte = function(nau) {
        $http.post("https://ciutadaestelar-g0uf.c9users.io/nau/", {
            id: nau,
        }).success(function(dades) {
            $scope.Nau = {};
            $scope.Nau.nom = dades.resposta.nom;
            $scope.Nau.resum = dades.resposta.descripcio;
            $scope.Nau.video = $sce.trustAsResourceUrl(dades.resposta.video);
        });
    };
});