$(document).ready(function() {
   $('#b-localarra').click(function() {
        $(this).attr('data-default', $(this).width());
        $(this).animate({ width: 950 }, 'slow');
        $('#1-localarra').hide();
        $('#2-localarra').hide();
        $('#3-localarra').hide();
        $('#4-localarra').hide();
        $('#5-localarra').hide();
    }).blur(function() {
        $(this).animate({ width: 200 }, 'slow');
        setTimeout( function() {$('#1-localarra').show();}, 235);
        setTimeout( function() {$('#2-localarra').show();}, 250);
        setTimeout( function() {$('#3-localarra').show();}, 280);
        setTimeout( function() {$('#4-localarra').show();}, 290);
        setTimeout( function() {$('#5-localarra').show();}, 300);
    });
   $( window ).resize(function() { 
    $(window).width(function() {
      if ($(window).width() < 925) {
        $('#h-localarra').css('padding-left','1em');
      }
      if ($(window).width() > 925) {
        $('#h-localarra').css('padding-left','10em');
      }
    });
  });
  $(window).scroll(function () { 
    if ($(window).scrollTop() > 0) {
      $('#nav_bar').addClass('navbar-fixed-top');
    }
    if ($(window).scrollTop() < 1) {
      $('#nav_bar').removeClass('navbar-fixed-top');
    }
  });
});