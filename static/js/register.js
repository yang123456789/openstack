identity = document.getElementsByTagName('span');
function register_form(){
    var register = document.register;
    var username = register.username.value;
    if(username == "") {
        identity[0].style.display = 'inline-block';
    }
    var phone = register.phone.value;
    if(phone == "") {
        identity[1].style.display = 'inline-block';
    }
    var password = register.password.value;
    if(password == "") {
        identity[2].style.display = 'inline-block';
    }
    var new_password = register.new_password.value;
    if(new_password == "") {
        identity[3].style.display = '';
    }
    var identify_code = register.identify_code.value;
    if(identify_code == "") {
        identity[4].style.display = 'inline-block';
        return false;
    }
    if(phone != '' && !phone.match(/^\d{3}-\d{8}|\d{4}-\d{7}$|^1(3[0-9]|5[012356789]|8[0-9]|4[57]|7[68])\d{8}$/)) {
        alert("手机号码不正确")
    }
    if(password != '' && !password.match(/^\w{6,20}$/)) {
        alert("密码不匹配")
        return false;
    }
    return true;
}

function password_identity() {
    var password = document.getElementById('password').value;
    var new_password = document.getElementById('new_password').value;
    if(new_password != password) {
        document.getElementsByTagName('span')[3].style.display = 'inline-block';
        document.getElementById('success').style.display = '';
    }
    else if(new_password == password && new_password != '') {
        document.getElementById('success').style.display = 'inline-block';
        document.getElementsByTagName('span')[3].style.display = '';
    }
}

function disappear_1() {
    identity[0].style.display = '';
}
function disappear_2() {
    identity[1].style.display = '';
}
function disappear_3() {
    identity[2].style.display = '';
}
function disappear_4() {
    identity[4].style.display = '';
}

input = document.getElementsByTagName('input');
function appear_1() {
    if(!input[1].value) {
        identity[0].style.display = 'inline-block';
    }
}
function appear_2() {
    if(!input[2].value) {
        identity[1].style.display = 'inline-block';
    }
}
function appear_3() {
    if(!input[3].value) {
        identity[2].style.display = 'inline-block';
    }
}
function appear_4() {
    if(!input[5].value) {
        identity[4].style.display = 'inline-block';
    }
}
