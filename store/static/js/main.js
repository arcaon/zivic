$(window).scroll(function() {
    if ( $(window).scrollTop() >= 100 ) {
        $('header').css('display', 'none');
        $('#nav').css({'position': 'fixed', 'top': '0', 'z-index': '100', 'width': '100%', 'margin': '0'});
        $('#cont').css('margin-top', '150px');
        $('#nav_cont').css('padding-left', '5%');
    }else{
        $('#nav').css({'position': 'static', 'top': 'none', 'z-index': '100', 'width': '70%', 'margin': '10px auto'});
        $('header').css('display', 'block');
        $('#cont').css({'margin-top': '0'});
        $('#nav_cont').css('padding-left', '0');
    }
});



