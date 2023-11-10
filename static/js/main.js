// Message notification timeout.
$(document).ready(function() {
    // messages timeout for 6 sec 
    setTimeout(function() {
        $('.messages').fadeOut(2000);
    }, 6000); // <-- time in milliseconds, 1000 =  1 sec

    // delete message
    $('.btn-close').live('click',function(){
        $('.btn-close').parent().attr('style', 'display:none;');
    })
});


// onclick Image Popup jQuery Lightbox Plugin
$(document).ready(function(){
    
	$("#imageGallery").imagePopup({
    overlay: "#e9ede9da",

    closeButton:{
        width: "40px",
        height:"40px"
    },
    imageBorder: "5px solid #264653",
    borderRadius: "10px",
    imageWidth: "500px",
    imageHeight: "400px",
    open: function(){
        console.log("opened");
    },
    close: function(){
        console.log("closed");
    }
});

});

// onclick Image Popup jQuery Lightbox Plugin
$(document).ready(function(){
    
	$("#imageGallery-mobile").imagePopup({
    overlay: "#e9ede9da",

    closeButton:{
        width: "40px",
        height:"40px"
    },
    imageBorder: "5px solid #264653",
    borderRadius: "10px",
    imageWidth: "300px",
    imageHeight: "250px",
    open: function(){
        console.log("opened");
    },
    close: function(){
        console.log("closed");
    }
});

});
