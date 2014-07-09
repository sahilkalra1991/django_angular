var Login = GlassWeb.controller('Login',

    ['$scope', 'Restangular', 'UserService','GW_CONSTANTS',

    function ($scope, Restangular, UserService, GW_CONSTS ) {
        //page specific variables
        $scope.page = {
            templateName: 'loginTemplateUrl'
        };

        $scope.user = {};       //user model
        //login status flag
        $scope.loginFailure = false;
        $scope.serverError = false;

        $scope.isLoading = false;       //login submission progress flag

        var login_user_service = new Restangular.one(GW_CONSTS.APIUrls['login_url']);

        //login handler
        $scope.login = function(){
            $scope.isLoading = true;

            var user = $scope.user;

            var service_dict = {
                username: user.user_name,
                password: user.password
            };
            var userService = new UserService();
            login_user_service.post('', service_dict).then(
                function(response){
                    $scope.isLoading = false;
                    var user_info = {
                        api_token: response.token,
                        full_name: response.full_name,
                        user_name: user.user_name
                    };
                    userService.setUserInfoStorage(user_info, true);
                }, function(response){
                    $scope.isLoading = false;
                    $scope.serverError = true;
                }
            );
        };
    }
]);