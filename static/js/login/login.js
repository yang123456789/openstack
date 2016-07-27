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
        //var username = $('.user').val();
        //var password = $('.password').val();
        //var params = {
        //    'username': username,
        //    'password': password
        //};
        $ajax({
            type: "post",
            url: "/login",
            data: {'username': customer_username, 'password': customer_password},
            success: function(msg) {
                console.log('qwe')
                $('form').form(msg)
            },
            error: function(data) {
                console.log('qwe')
                var span_error = $('.error');
                span_error[0].innerHTML = '用户名或密码错误!';
                return false;
            }
        });
    };
    disappear = function() {
        var span_error = $('.error');
        span_error[0].innerHTML = '';
    }
})(jQuery);