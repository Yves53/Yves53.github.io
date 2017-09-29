$('.comments').hide();

$('.cmt').unbind('click').click(function () {
   $('.comments').slideDown()
});

$('.hidecomment').click(function () {
   $('.comments').slideUp()
});
