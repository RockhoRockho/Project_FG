function eventHandler(e) {
    var $eTarget = $(e.currentTarget);
    var $targetPanel = $('[aria-labelledby="' + $eTarget.attr('id') + '"]');
  
    // 조건문으로 이벤트 구분
    if (e.type === 'click') { // 클릭 시 동작
      $eTarget
        .attr('aria-selected', true)
        .addClass('active')
        .siblings('[role="tab"]')
        .attr('aria-selected', false)
        .removeClass('active');
  
      $targetPanel
        .attr('aria-hidden', false)
        .addClass('active')
        .siblings('[role="tabpanel"]')
        .attr('aria-hidden', true)
        .removeClass('active');
    } else if (e.type === 'keydown' && e.which === 13) { // 키가 눌렸을 때 && 키가 엔터일 때
      // e.which 는 keycode 값을 판별하는데 13 이 엔터 키에 해당되는 keycode
      $(this).click(); // 현재 Element에 클릭이벤트 발생시킴
    }
  }
  
  // 바인딩에 keydown 이벤트 추가 - 쉼표 없음
  $('[role="tab"]').on('click keydown', eventHandler);