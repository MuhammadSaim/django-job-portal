
# a function to check request is ajax or not
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'
