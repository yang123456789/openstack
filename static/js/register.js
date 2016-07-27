function change_code() {
        var code = document.getElementById('check_code');
        code.src += '?';
    }
    window.onload = function() {
        var username = document.getElementById('id_username');
        var phone = document.getElementById('id_phone');
        var identify_code = document.getElementById('id_identify_code');
        username.value = '';
        phone.value = '';
        identify_code.value = '';
    };

function register(){
    var register = document.register;
    var username = register.username.value;
    if(username == ''){
        alert('用户名不能为空');
        return false;
    }
    var phone = register.phone.value;
    if(!phone.match(/^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$/)){
        alert('手机号码不正确');
        return false;
    }
    var password = register.password.value;
    if(password == ''){
        alert('密码不能为空');
        return false;
    }
    else if(!qq.match(/^\w{8,20}$/)){
        alert('密码不少于8位且是数字字母的组合')
        return false;
    }
    var again_password = register.again_password.value;
    if(again_password != password){
        alert('密码不正确');
        return false;
    }
    var identity_code = register.identify_code.value;
    if(identity_code == ''){
        alert('验证码不能为空');
        return false;
    }
    return true;
}