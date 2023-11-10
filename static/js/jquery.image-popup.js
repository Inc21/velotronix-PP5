(function($){
    $.fn.imagePopup = function(options){   

        var settings = $.extend({
            overlay: "rgba(0, 0, 0, 0.5)",
            closeButton: {
                src: null,
                width: "30px",
                height:"30px"
            },
            imageBorder: "5px solid #ffffff",
            borderRadius: "5px",
            imageWidth: "500px",
            imageHeight: "400px",
            imageCaption: {
                exist: true,
                color: "#ffffff",
                fontSize: "20px"
            },
            open: null,
            close: null
        }, options);
        
    
        return this.each(function(){
            var $overlay, $closeButton, $image, $imageCaption;
            setOverlayProperties();
            setCloseButtonProperties();
            setImageProperties();

            $(this).find("a").on("click", function(event){
                event.preventDefault();    
                var imageSource = $(this).children("img").attr("src");
                $image.attr("src", imageSource);

                if(settings.imageCaption.exist !== true){
                    var caption = $(this).children("img").attr("alt");
                    $imageCaption.text(caption);
                }

                if($.isFunction(settings.open)){    
                    settings.open.call(this);
                }

                $overlay.css({opacity: 0.1}).show().animate({opacity: 1});
            });

            function setImageProperties(){
                $image = $('<img>');
                $image.css(
                    {
                        "width": settings.imageWidth,
                        "height": settings.imageHeight,
                        "border": settings.imageBorder,
                        "border-radius": settings.borderRadius
                    }
                )
                $overlay.append($image);

                if(settings.imageCaption.exist == true){
                    $imageCaption = $('<p></p>');
                    $imageCaption.css({
                        "color": settings.imageCaption.color,
                        "font-size": settings.imageCaption.fontSize
                    });

                    $overlay.append($imageCaption);
                };
            };

            function setOverlayProperties(){
                $overlay = $('<div></div>'); 
                $overlay.css({
                    "background": settings.overlay,
                    "opacity": 1,
                    "position": "absolute",
                    "top": "0px",
                    "left": "0px",
                    "display": "none",
                    "text-align": "center",
                    "width": "100%",
                    "height": "100%",
                    "padding-top": "5%",
                    "z-index": "9999"
                });
                $("body").append($overlay);
            };
            
            function setCloseButtonProperties(){ 
                var prop = {
                    "color": "white",
                    "cursor": "pointer",
                    "font-size": "20px",
                    "width": settings.closeButton.width,
                    "height": settings.closeButton.height,
                    "position": "relative",
                    "top": "-160px",
                    "right": "-496px",
                    "color": "#ffffff",
                    "font-size": "40px",
                    "font-weight": "bold",
                    "padding": "2px 12px 2px 12px",
                    "border-radius": "0 5px",
                    "background": "#d9534f",
                    "border": "0px",
                    "z-index": "1"
                };
            

                if(settings.closeButton.src) {
                    $closeButton = $("<img>");
                    $closeButton.attr("src", settings.closeButton.src);
                } else {
                    $closeButton = $("<span>X</span>");
                }

                
                $closeButton.css(prop);
                
                $overlay.append($closeButton);
            };

            $closeButton.click(function(){  
                if($.isFunction(settings.close)){
                    settings.close.call(this);
                };

                $overlay.animate({opacity: 0.1}, function(){
                    $overlay.hide();
                });               
            });
        });
    };
}(jQuery));
