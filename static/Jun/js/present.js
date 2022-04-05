$(function () {
  var tabContainer = document.querySelector('.tab__container');
  if (!tabContainer) return;

  $(tabContainer).on('click', '.tab__button', handleClickEvent);
  $(tabContainer).on('keydown', '.tab__list', handleKeyEvent);

  function handleClickEvent(event) {
    event = event || window.event;
    event.stopPropagation();
    var currTab = event.currentTarget;

    activateTab(currTab);
    activateTabPanel(currTab);
  }

  function activateTab(tab) {
    if (!tab) return;

    $(tab)
      .addClass('tab__button-active')
      .attr({
        'tabindex': '0',
        'aria-selected': 'true'
      })
      .focus()
      .siblings()
      .removeClass('tab__button-active')
      .attr({
        'tabindex': '-1',
        'aria-selected': 'false'
      })
  }

  function activateTabPanel(tab) {
    if (!tab) return;
    $('#' + tab.getAttribute('aria-controls'))
      .attr({
        'tabindex': '0'
      })
      .prop({
        'hidden': false
      })
      .addClass('tab__panel-active')
      .siblings('.tab__panel')
      .removeClass('tab__panel-active')
      .attr({
        'tabindex': '-1'
      })
      .prop({
        'hidden': true
      })
  }

  function handleKeyEvent(event) {
    event = event || window.event;
    event.stopPropagation();
    var keycode = event.keycode || event.which;

    switch (keycode) {
      case 37:
        if (event.target.previousElementSibling) {
          $(event.target)
            .attr({
              'tabindex': '-1'
            })
            .prev()
            .attr({
              'tabindex': '0'
            })
            .focus()
        } else {
          $(event.target)
            .attr({
              'tabindex': '-1'
            })
            .siblings(':last')
            .attr({
              'tabindex': '0'
            })
            .focus()
        }
        break;
      case 39:
        if (event.target.nextElementSibling) {
          $(event.target)
            .attr({
              'tabindex': '-1'
            })
            .next()
            .attr({
              'tabindex': '0'
            })
            .focus()
        } else {
          $(event.target)
            .attr({
              'tabindex': '-1'
            })
            .siblings(':first')
            .attr({
              'tabindex': '0'
            })
            .focus()
        }
        break;
      case 32:
      case 13:
        event.preventDefault();
        activateTab(event.target);
        activateTabPanel(event.target);
        break;
    }
  }
});

var mRadio = document.getElementsByClassName('message_radio');

var giftImage = document.querySelector('.gift_img')
var giftform = document.querySelector('.gift_message')

function handleClick(element) {
  giftform.style.backgroundColor = element.currentTarget.dataset['backgroundColor']
  giftform.style.color = element.currentTarget.dataset['fontColor']
  giftImage.src = element.currentTarget.dataset['imgSrc']
}

for (var i = 0; i < mRadio.length; i++) {
  mRadio[i].firstElementChild.addEventListener('change', handleClick);
}