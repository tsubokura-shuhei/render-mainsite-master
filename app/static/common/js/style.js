
function load_effect() {
  var element = document.getElementsByClassName('load-fade');
  if(!element) return; // 要素がない場合は終了
  
  for(var i = 0; i < element.length; i++) { 
    element[i].classList.add('is-show');
  }
}
setTimeout(load_effect, 600); // 600ミリ秒経過後に実行


// rotate()
document.querySelector(`.rotate`).animate(
    [
      { transform: 'rotate(0deg)' },
      { transform: 'rotate(360deg)' }
    ],
    {
      duration: 10000,
      easing: 'linear',
      iterations: Infinity
    }
  );

// 表示モーション
  function load_effect() {
    var element = document.getElementsByClassName('load-fade');
    if(!element) return; // 要素がない場合は終了
    
    for(var i = 0; i < element.length; i++) { 
      element[i].classList.add('is-show');
    }
  }
  setTimeout(load_effect, 100); // 600ミリ秒経過後に実行

function scroll_effect(){
  var element = document.getElementsByClassName('main_scroll_up');
  if(!element) return;

  var scrollY = window.pageYOffset;
  var windowH = window.innerHeight;
  var showTiming = 200;
  for(var i = 0; i < element.length; i++){
    var elemClientRect = element[i].getBoundingClientRect();
    var elemY = scrollY + elemClientRect.top;
    if(scrollY > elemY - windowH + showTiming){
      element[i].classList.add('main-show');
    }
  }
}
window.addEventListener('scroll', scroll_effect);