$(document).ready(function() {


    /* For the sticky navigation */
    $('.js_section_cours').waypoint(function(direction) {
        if (direction == "down") {
            $(".header_main_nav").toggleClass('header_main_nav_sticky');
        } else {
            $('nav').removeClass('header_main_nav_sticky');
        }
    }, {
      offset: '60px;'
    });

    $(function() {
       $(".nav_social_icons").click(function() {
         $(".nav_side_bar_btns").toggleClass('nav_side_bar_btns-open');
       });
     });
    /*$(function(){
        $(".js__menu_button_small_size").click(function(){
            var icon = $(".js__menu_button_small_size ion-icon");
            $(".nav_drop_menu").slideToggle(200);

            if (icon.has("menu")) {
                icon.replaceWith("");
            }

        });
    });*/
    $('.js__menu_button_small_size').click(function() {
        var nav = $('.nav_drop_menu');
        var icon = $('.js__menu_button_small_size i');

        nav.slideToggle(200);

        if (icon.hasClass('ion-navicon-round')) {
            icon.addClass('ion-close-round');
            icon.removeClass('ion-navicon-round');
        } else {
            icon.addClass('ion-navicon-round');
            icon.removeClass('ion-close-round');
        }
    });

    $(function () {
        $('#sidebarCollapse').on('click', function () {
            $('#sidebar1').toggleClass('active');
            $(this).toggleClass('active');
        });
    });

});
