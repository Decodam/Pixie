
// carousel
var owl = $('.owl-carousel');
owl.owlCarousel({
    loop:false,
    responsive:{ 
        0:{
            items:1
        },  
        315:{
            items:2
        },  
        355:{
            items:3
        },  
        465:{
            items:4
        },  
        575:{
            items:5
        },  
        695:{
            items:6
        },
    }
});
owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.deltaY>0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});