(function($) {
    openstack_login = function() {
        var username = $('.user').val();
        var password = $('.password').val();
        var error = ['用户名不能为空!', '密码不能为空!'];
        var span_error = $('.error');
        if (username == "") {
            span_error[0].innerHTML = error[0];
            return false;
        }
        if (password == "" && username != "") {
            span_error[0].innerHTML = error[1];
            return false;
        }
        return true;
    };
    transmission_data = function() {
        var username = $('.user').val();
        var password = $('.password').val();
        var params = {
            'customer_username': username,
            'customer_password': password
        };
        $ajax({
            type: "POST",
            url: "/login",
            data: params,
            success: function(msg) {
                $('form').html(msg)
            },
            error: function(msg) {
                var span_error = $('.error');
                span_error[0].innerHTML = '用户名或密码错误!';
            }
        });
    };
    disappear = function() {
        var span_error = $('.error');
        span_error[0].innerHTML = '';
    }
})(jQuery);