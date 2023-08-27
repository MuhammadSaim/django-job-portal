// require jquery
window.$ = window.jQuery = require("jquery");

// nice toast css https://www.jqueryscript.net/other/alert-nice-toast.html
import "../../libs/nice-toast/js/nice-toast-js";



// setup ajax setup for CSRF Token in all ajax request
$.ajaxSetup({
    headers: {
        'X-CSRFToken': $('meta[name="csrf-token"]').attr('content')
    },
});


// add notification to the window object to available all over the application
window.notification = (
    message,
    type = 'info',
    pos = 'top-right',
    duration = 2000
) => {

    $.niceToast.setup({
        position: pos,
        timeout: duration,
    });

    if (type === 'info'){
        $.niceToast.info(message);
    }

    if(type === 'warning'){
        $.niceToast.warning(message);
    }

    if(type === 'error'){
        $.niceToast.error(message);
    }

    if(type === 'success'){
        $.niceToast.success(message);
    }

};



// a spinner for the ajax form
const spinner = `<div class="spinner-border text-light spinner-border-sm" role="status"></div>`;

// ajax form requests
$(".ajax-form").on('submit', function (e) {

    e.preventDefault();

    const url = $(this).attr('action');
    const method = $(this).attr('method');
    const payload = $(this).serializeArray();
    const is_redirect = $(this).data('redirect');
    const is_refresh = $(this).data('refresh');
    let submit_btn = $(this).find("button[type=submit]");
    let submit_html = submit_btn.html();
    $(this).find("input, select, button, textarea").attr("disabled", true);

    $.ajax({
        url: url,
        method: method,
        data: payload,
        beforeSend: () => {
            $(this).find("input, select, textarea").removeClass("is-invalid");
            submit_btn.html(spinner);
        },
        success: (data) => {
            $(this)
                .find("input, select, button, textarea")
                .attr("disabled", false);
            submit_btn.html(submit_html);
            if (data.error && data.form) {
                let messages = data.messages;
                Object.keys(messages).forEach((key) => {
                    $(this).find('#' + key).addClass('is-invalid');
                    $(this).find('.' + key + "-feedback").text(Object.values(messages[key])[0]);
                });
            } else {
                if(data.error){
                    notification(data.messages, 'error');
                }else{
                    notification(data.messages, 'success');
                    $(this).trigger("reset");
                    if (is_refresh) {
                        setTimeout(function () {
                            location.reload();
                        }, 2500);
                    }
                    if (is_redirect) {
                        notification("Redirecting...");
                        setTimeout(() => {
                            location.href = data.redirect_url;
                        }, 3000);
                    }
                }
            }
        }
    });


});


