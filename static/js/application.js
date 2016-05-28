function get_csrf_token() {
    return $("input[name='csrfmiddlewaretoken']").val();
}

function add_csrf_token(data) {
    data["csrfmiddlewaretoken"] = get_csrf_token();
    return data;
}