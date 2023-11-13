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
    imageWidth: "500",
    imageHeight: "400px",
    open: function(){
        console.log("opened");
    },
    close: function(){
        console.log("closed");
    }
});
});

// Back to top button
var btt = $('.btt-button');
var deliveryBanner = $('.delivery-banner');
$(window).scroll(function() {
    if ($(window).scrollTop() > 200) {
        btt.removeClass('d-none');
        deliveryBanner.addClass('d-none');
    } else {
        btt.addClass('d-none');
        deliveryBanner.removeClass('d-none');
    }
});
$('.btt-button').click(function(e) {
    window.scrollTo(0, 0);
})

// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    var currentValue = parseInt($(`#id_qty_${itemId}`).val());
    var minusDisabled = currentValue < 2;
    var plusDisabled = currentValue > 98;
    $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
    $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
var allQtyInputs = $('.qty_input');
for(var i = 0; i < allQtyInputs.length; i++){
    var itemId = $(allQtyInputs[i]).data('item_id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.qty_input').change(function() {
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-qty').click(function(e) {
    e.preventDefault();
    var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
    var currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    var itemId = $(this).data('item_id');
    handleEnableDisable(itemId);
});
