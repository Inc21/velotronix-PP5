$(document).ready(function() {
    // messages timeout for 10 sec 
    setTimeout(function() {
        $('.messages').fadeOut('slow');
    }, 10000); // <-- time in milliseconds, 1000 =  1 sec

    // delete message
    $('.btn-close').live('click',function(){
        $('.btn-close').parent().attr('style', 'display:none;');
    })
});