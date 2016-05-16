function register_form(){
    var register = document.register;
    var identity = document.getElementsByTagName('span');
    var username = register.username.value;
    if(username == "") {
        identity[0].style.display = 'inline-block';
        identity[0].style.width = '130px';
    }
    var phone = register.phone.value;
    if(phone == "") {
        identity[1].style.display = 'inline-block';
        identity[1].style.width = '130px';
    }
    var password = register.password.value;
    if(password == "") {
        identity[2].style.display = 'inline-block';
        identity[2].style.width = '130px';
    }
    var newpassword = register.newpassword.value;
    if(newpassword == "") {
        identity[3].style.display = '';
        identity[3].style.width = '130px';
    }
    var identifycode = register.identifycode.value;
    if(identifycode == "") {
        identity[4].style.display = 'inline-block';
        identity[4].style.width = '130px';
        return false;
    }
    if(phone != '' && !phone.match(/^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$/)) {
        alert("手机号码不正确")
        return false;
    }
    if(password != '' && !password.match(/^\w{6,20}$/)) {
        alert("密码不匹配")
        return false;
    }
    return true;
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