window.$ = window.jQuery = require("jquery");


$.ajaxSetup({
    headers: {
        'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
    },
});


// ajax form requests
$(".ajax-form").on('submit', function(e){

    e.preventDefault();

    const url = $(this).attr('action');
    const method = $(this).attr('method');
    const is_redirect = $(this).data('redirect');
    const is_refresh = $(this).data('refresh');
    let submit_btn = $(this).find("button[type=submit]");
    let submit_html = submit_btn.html();
    $(this).find("input, select, button, textarea").attr("disabled", true);


});