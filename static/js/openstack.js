(function($) {
    var global = jQuery.noConflict(true);
    var second_floor_1 = global('.second_floor_1');
    var second_floor_2 = global('.second_floor_2');
    var second_floor_3 = global('.second_floor_3');
    var second_floor_4 = global('.second_floor_4');
    var identity = global('dl dd');
    var tab_down_1 = global('.tab-down-1');
    var tab_right_1 = global('.tab-right-1');
    global('.first_floor_1').click(function() {
        second_floor_1.toggleClass('success');
        //tab_down_1.css({'-moz-transform':'rotate(90deg)',
        //                '-webkit-transform':'rotate(90deg)',
        //'-o-transform':'rotate(90deg)',
        //'transform':'rotate(90deg)',
        //'filter':'progid:DXImageTransform.Microsoft.BasicImage(rotation=1)'});
        //tab_right_1.toggleClass('success')
        second_floor_1.css('width', '120px');
        second_floor_2.toggle();
        second_floor_2.css('width', '120px');
    });
    global('.first_floor_2').click(function() {
        second_floor_3.toggle();
        second_floor_3.css('width', '120px');
        second_floor_4.toggle();
        second_floor_4.css('width', '120px');
    });
    global('.first_floor_3').click(function() {
        identity.toggle();
        identity.css('width', '120px');
    });

    var third_floor_1 = global('.third_floor_1 li');
    second_floor_1.click(function() {
        third_floor_1.toggle();
        third_floor_1.css('width', '120px');
    });
    var third_floor_2 = global('.third_floor_2 li');
    second_floor_2.click(function() {
        third_floor_2.toggle();
        third_floor_2.css('width', '120px');
    });
    var third_floor_3 = global('.third_floor_3 li');
    second_floor_3.click(function() {
        third_floor_3.toggle();
        third_floor_3.css('width', '120px');
    });
    var third_floor_4 = global('.third_floor_4 li');
    second_floor_4.click(function() {
        third_floor_4.toggle();
        third_floor_4.css('width', '120px');
    });
    var header_right = $('.header-right');
    var head_right = global('.head-right');
    header_right.mouseover(function() {
        head_right.toggle();
        global('.head-right dt').css({'width': '100px','text-indent': '-25px','display': 'inline-block'})
    })
})(jQuery);
