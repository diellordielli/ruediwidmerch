$(function(){

    var $container = $('#container');
        $items = $('.item');
  
    $container.isotope({
        itemSelector: '.item',
        masonry: {
            columnWidth: 60
        }
    })

    $(window).on('load', function() {
        $container.isotope( 'reLayout' );
    });

    $('.item.portrait').click(function(){
        var $this = $(this),
            tileStyle = $this.hasClass('big');
        $this.toggleClass('big');

        $this.find('.portraitdesc').toggle();
        $this.find('.portraitsubtitle').toggle();
        $this.find('.portraittitle').toggleClass('portraittitle2');
        $container.isotope( 'reLayout' )

    });

    $('.item.category').click(function() {
        if ( $container.data('filter') === 'all') {
            var category = $(this).attr('title');
            
            $container.isotope({ filter: "." + category });
            $container.data('filter', category);

            var $this = $(this);
            $this.find('.categoryclose').css({'display': 'inline'});
        } else {
            var selector = $('.item');
                $this = $(this);

            $container.isotope({ filter: selector });
            $container.data('filter', 'all');

            $this.find('.categoryclose').hide();
        }

     });

    $('.item').mouseenter(function() {
        var $this = $(this);

        $this.find('.imagetext').fadeIn();
    });

    $('.item').mouseleave(function() {
        var $this = $(this);

        $this.find('.imagetext').fadeOut();
    });
});