function register_form(){
    var register = document.register;
    var identity = document.getElementsByTagName('span');
    var input = document.getElementsByTagName('input');
    for(var i=0;i < identity.length;i++) {
        if(!input[i+1].value) {
            identity[i].style.display = 'inline-block';
            identity[i].style.width = '130px';
        }
        if(i == 3) {
            if(identity[i]) {
                identity[i].style.display = '';
            }
        }
    }
    var phone = register.phone.value;
    if(!phone.match(/^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$/)) {
        alert("手机号码不正确")
        return false;
    }
    var password = register.password.value;
    if(!password.match(/^\w{6,20}$/)) {
        alert("密码不匹配")
        return false;
    }
};

function password_identity() {
    var password = document.getElementById('password').value;
    var newpassword = document.getElementById('newpassword').value;
    if(newpassword != password) {
        document.getElementsByTagName('span')[3].style.display = 'inline-block';
    }
    else {
        document.getElementById('success').style.display = 'inline-block';
    }
};