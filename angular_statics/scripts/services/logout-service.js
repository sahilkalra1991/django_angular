GlassWeb.service('LogoutService',

    ['$location','$localStorage','ipCookie',

    function ($location,$localStorage,ipCookie) {
        return {
            logout: function(){
                delete $localStorage.user_info;
                ipCookie.remove('logged_in');
                $location.url("/");
            }
        };
}]);
