GlassWeb.factory('UserService', ['$location','$localStorage','ipCookie',

    function($location,$localStorage,ipCookie){
        return function(){
            //sets the login cookie
            this.setUserInfoStorage = function(user_info_dict, redirectToHome){
                $localStorage.user_info = user_info_dict;
                ipCookie('logged_in',true);
                if(redirectToHome){
                    $location.url("/home");
                }
            };
        }
    }
]);
