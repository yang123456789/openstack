(function($) {
    var global = jQuery.noConflict(true);
    var second_floor_1 = global('.second_floor_1');
    var second_floor_2 = global('.second_floor_2');
    var second_floor_3 = global('.second_floor_3');
    var second_floor_4 = global('.second_floor_4');
    var identity = global('.identity');
    global('.first_floor_1').click(function() {
        second_floor_1.toggleClass('success');
        second_floor_2.toggleClass('success');
    });
    global('.first_floor_2').click(function() {
        second_floor_3.toggleClass('success');
        second_floor_4.toggleClass('success');
    });
    global('.first_floor_3').click(function() {
        //identity.toggleClass('success')
        //identity_1.toggleClass('success')
        //identity_2.toggleClass('success')
    });
})(jQuery);
