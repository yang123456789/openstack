(function($) {
    openstack_login = function() {
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        var code = $('input[name="code"]').val();
        var params = {
            'username': username,
            'password': password,
            'code': code
        };
        $.ajax({
            type: "GET",
            url: "login/validate",
            data: params,
            success: function(result) {
                if(result['data'].indexOf(username) == -1) {

                }
                if(result['data'].indexOf(password) == -1) {

                }
            }
        });
    };
})(jQuery);