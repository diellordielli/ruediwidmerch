$(document).ready(function() {
    $('.fancybox').on('click', function(event) {
        event.preventDefault();

        var $this = $(this);
            activeFilter = $('#container').data('filter') || 'cartoon',
            $group = $('.' + activeFilter + ' a');

        $.fancybox($group, {
            type: 'ajax',
            index: $group.index(this),
            autoSize: false,
            afterLoad: function() {
                var imgDimensions = getImageDimensions(this.element.find('img').attr('src'));

                this.width = imgDimensions.width;
            }
        });
       
    });

});

function getImageDimensions(src) {
        // Create new offscreen image to test
        var theImage = new Image();
        theImage.src = src;

        return {
            width: theImage.width,
            height: theImage.height
        }
}