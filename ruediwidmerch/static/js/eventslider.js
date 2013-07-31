var carouselOptions = {
    speed: 400,
    imageRatio: 1
}

$(window).load(function() {
    var eventHeight = $('.eventcontainer').outerHeight();
    $('.eventouter').height(eventHeight);
});

$(document).ready(function() {
    // gets updated on resize and on page load
    var totalWidth, totalElemnts, stepWidth, navpos = 0

    resize();

    $(window).resize(function() {
        resize();
    });

    function resize() {
        var regionGrey = $('.eventall').width(),
            newsWidth = Math.round(regionGrey * carouselOptions.imageRatio),
            eventSingle = $('.eventsingle').width();

        $('.eventcontainer').width(newsWidth);

        var eventSingleWidth = (newsWidth - 120);
        $('.eventsingle').css('width', eventSingleWidth + 'px')

        var marginleft = (regionGrey - newsWidth) / 2;
        $('.eventcontainer').css('margin-left', marginleft + 'px');

        var marginright = (regionGrey - newsWidth) / 2;
        $('.eventcontainer').css('margin-right', marginright + 'px');

        // set superscope totalWidth
        stepWidth = $(".eventinner > .eventcontainer:first").outerWidth(true);
        totalElemnts = $(".eventinner > .eventcontainer").length;
        totalWidth = (stepWidth * totalElemnts);

        $(".eventinner").width(totalWidth);

        $('.eventinner').css('margin-left', - navpos * stepWidth);

    $('.navright').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;
        
        var nextContainerHeight = $(".eventcontainer").eq(navpos).outerHeight();

        $('.eventouter').animate({'height': nextContainerHeight});
        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);

    });

    }

    $('.navleft').on('click', function(event) {
        event.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalElemnts -1) * stepWidth;
        }

        navpos = -newLeft / stepWidth;

        var nextContainerHeight = $(".eventcontainer").eq(navpos).outerHeight();

        $('.eventouter').animate({'height': nextContainerHeight});
        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

    Hammer('.archiveouter').on("swipeleft", function(ev) {
        ev.gesture.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft - stepWidth;

        if (newLeft <= -totalWidth) {
            newLeft = 0;
        }

        navpos = -newLeft / stepWidth;
        
        var nextContainerHeight = $(".eventcontainer").eq(navpos).outerHeight();

        $('.eventouter').animate({'height': nextContainerHeight});
        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);

    });


    Hammer('.archiveouter').on("swiperight", function(ev) {
        ev.gesture.preventDefault();
        var newLeft = $('.eventinner').get(0).offsetLeft + stepWidth;

        if (newLeft > 0) {
            newLeft = -(totalElemnts -1) * stepWidth;
        }

        navpos = -newLeft / stepWidth;

        var nextContainerHeight = $(".eventcontainer").eq(navpos).outerHeight();

        $('.eventouter').animate({'height': nextContainerHeight});
        $('.eventinner').animate({'margin-left': newLeft}, carouselOptions.speed);
    });

});