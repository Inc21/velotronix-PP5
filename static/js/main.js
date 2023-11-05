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