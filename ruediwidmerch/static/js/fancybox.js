$(document).ready(function() {
    $('.fancybox').on('click', function(event) {
        event.preventDefault();

        var $this = $(this);
            activeFilter = $('#container').data('filter') || 'cartoon',
            $group = $('.' + activeFilter + ' a');

        // Get on screen image
        var screenImage = $this.find('img');

        // Create new offscreen image to test
        var theImage = new Image();
        theImage.src = screenImage.attr("src");

        // Get accurate measurements from that.
        var imageWidth = theImage.width;
        var imageHeight = theImage.height;

        $.fancybox($group, {
            type: 'ajax',
            index: $group.index(this),
            autoSize: false,
            width: imageWidth,
            height: imageHeight
        });
       
    });

});