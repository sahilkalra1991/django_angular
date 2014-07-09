'use strict';

GlassWeb.config(['$routeProvider', 'RestangularProvider','GW_CONSTANTS','$httpProvider',
    function ($routeProvider,RestangularProvider,GW_CONSTS,$httpProvider) {
        //url routing configurations
        var basePageUrl = GW_CONSTS.templateUrls['basePageUrl'];
        $routeProvider.
            when("/logout", {
                resolve: {
                    logout: function (LogoutService) {
                        LogoutService.logout();
                    }
                }
            }).
            when("/home", {
                templateUrl: basePageUrl,
                controller: "HomePage"
            }).
            when("/", {
                templateUrl: basePageUrl,
                controller: "Login"
            }).
            otherwise({
                redirectTo: '/'
            });

        //set default params
        RestangularProvider.setDefaultRequestParams(
            GW_CONSTS["defaultRequestParams"]);

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

}]).run(['$rootScope','GW_CONSTANTS','$location','$localStorage','ipCookie',
    function($rootScope,GW_CONSTS,$location,$localStorage,ipCookie) {
        //keys for constants to be added to $rootScope
        var GW_CONSTS_TO_ADD = ['templateUrls'];

        _.extend($rootScope, _.pick(GW_CONSTS, GW_CONSTS_TO_ADD));

        if($localStorage.user_info && !ipCookie('logged_in'))
            delete $localStorage.user_info;

        //Redirection based on permission
        $rootScope.$on( "$routeChangeStart", function(event, next, current) {
            var nextController = next.$$route.controller;
            if(nextController){
                if($localStorage.user_info){
                    //Redirect a authenticated user trying to access login page to home page
                    if (nextController=='Login'){
                        $location.url("/home");
                    }
                }else{
                    //Redirect a non-authenticated user trying to access a restricted page to login page
                    if (nextController!='Login'){
                        $location.url("/");
                    }
                }
            }
        });
}]);
