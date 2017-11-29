$('#owl-slider').owlCarousel({
        items:1,
        loop:true,
        center:true,
        margin:10,
        autoplay:true,
        autoplayTimeout:4000,
        URLhashListener:true,
        autoplayHoverPause:true,
        startPosition: 'URLHash',
    });

$('#speaker-carousel').owlCarousel({
    loop:true,
    margin:10,
    // center:true,
    autoplay:true,
    autoplayTimeout:6000,
    responsive:{
        0:{
            items:2
        },
        300:{
            items:2
        },
        600:{
            items:3
        },
        900:{
            items:3
        },
        1050:{
            items:4
        },
        1200:{
            items:4
        }
    }
})

