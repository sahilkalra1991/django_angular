var formValidationDirective = function() {
    return {
        restrict: 'E',
        require: '?ngModel',
        link: function(scope, elm, attr, ngModelCtrl) {
            if(ngModelCtrl){
                var allowedTypes = ['text', 'email', 'password'];
                if (allowedTypes.indexOf(attr.type)  === -1) {
                    return;
                }

                elm.on('blur', function() {
                    elm.removeClass('first-edit');
                    scope.$apply(function() {
                        ngModelCtrl.edited = ngModelCtrl.$dirty;
                    });
                });

                elm.on('focus', function() {
                    if(!ngModelCtrl.edited){
                        elm.addClass('first-edit');
                    }
                });
            }
        }
    };
};

GlassWeb.directive('input', formValidationDirective);