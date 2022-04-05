var stickyOrder = $('.order_sticky').offset();

$(window).scroll(function() {
  if ($(document).scrollTop() > stickyOrder.top) {
    $('.order_sticky').addClass('is_fixed');
  }
  else {
    $('.order_sticky').removeClass('is_fixed')
  }
})