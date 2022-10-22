$('.burger-btn').on('click',function(){//.btn_triggerをクリックすると
    $('.burger-btn').toggleClass('close');//.btn_triggerにcloseクラスを付与(ボタンのアニメーション)
    $('.nav-wrapper').toggleClass('fade');//.nav-wrapperに
    $('body').toggleClass('noscroll');//bodyにnoscrollクラスを付与(スクロールを固定)
   });

$('.autoplay').slick({
    fade:true,
    // slidesToShow: 1,
    slidesToScroll:1,
    autoplay: true,
    autoplaySpeed: 4000,
    // 画像下のドット（ページ送り）を表示
    dots: true,
    pauseOnHover: false,
});

