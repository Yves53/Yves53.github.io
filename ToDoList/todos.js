$("ul").on("click", "li", function () {
    $(this).toggleClass("clicked")
});

$("ul").on("click", "span", function (event) {
    $(this).parent().fadeOut(500, function () {
        $(this).remove();
    });
    event.stopPropagation();
});

$("input[type = 'text']").on("keypress", function (evt) {
    if(evt.which === 13) {
        var list = $(this).val();
        $("ul").append("<li><span><i class='fa fa-trash'></i></span> " + list + "</li>");
        $(this).val("");
    }
});

$(".fa-plus").click(function () {

    $("input").fadeToggle();

});