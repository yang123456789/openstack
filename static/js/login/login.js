(function($) {
    login = function() {
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        var captcha = $('input[name="captcha"]').val();
        if (validate_inputs(username, password, captcha)) {
            do_login(username, password, captcha)
        }
    };

    validate_inputs = function(username, password, captcha) {
        if (username == '') {
            render_error('用户名不能为空');
            $('#username').focus();
            return false;
        }
        if (password == '') {
            render_error('密码不能为空');
            $('#password').focus();
            return false;
        }
        if (captcha == '') {
            render_error('验证码不能为空');
            $("#J_codetext").focus();
            return false;
        }
        if (captcha.length < 4 || captcha.length > 4) {
            render_error('验证码错误')
            $("#J_codetext").focus();
            return false;
        }
    };

    do_login = function(username, password, captcha) {
        var params = {
            'username': username,
            'password': password,
            'captcha': captcha
        };
        $.ajax({
            type: "GET",
            url: "login/validate",
            data: params,
            success: function(result) {
                if(result['data'].indexOf(username) == -1) {
                    $('#info').html('用户名不正确')
                }
                else if(result['data'].indexOf(password) == -1) {
                    $('#info').html('密码不正确')
                }
            }
        });
    }

    render_error = function(error_message) {
        var elem_error = $('#error_message');
        elem_error.html(error_message);
        elem_error.show();
    }
})(jQuery);