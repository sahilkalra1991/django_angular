var HomePage = GlassWeb.controller('HomePage',

    ['$scope', 'Restangular', '$routeParams', '$localStorage',

    function($scope, Restangular, $routeParams, $localStorage){

        //page specific variables
        $scope.page = {
            templateName: 'homeTemplateUrl'
        };

        $scope.user = $localStorage.user_info;
        var user = $scope.user;
    }
]);
