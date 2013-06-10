$(document).ready(function() {
    $(document).ready(function() {
        $(".fancybox").fancybox({
            helpers: {
                title: {
                    type: "under"
                }
            },
            afterShow: function() {
                var imageWidth = $(".fancybox-inner").width();
                $(".fancybox-title-over-wrap").css({
                    "width": imageWidth,
                    "paddingLeft": 0,
                    "paddingRight": 0,
                    "textAlign": "center"
                });
            }

        });
    });
}); // ready