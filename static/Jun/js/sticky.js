var stickyOrder = $('.order_sticky').offset();

$(window).scroll(function() {
  if ($(document).scrollTop() > stickyOrder.top) {
    $('.order_sticky').addClass('is_fixed');
    $('.order_agree').css('margin-top', '360px')
  }
  else {
    $('.order_sticky').removeClass('is_fixed')
    $('.order_agree').css('margin-top', '60px')
  }
})