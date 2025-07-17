from django.http import HttpResponse


# Create your views here.
def simple_test(request):
    return HttpResponse('This is the test page')


def simple_test_post(request):
    if request.method == 'POST':
        decoded_data = request.body.decode('utf-8')
        print(decoded_data)
        return HttpResponse('Data was recieved!')
    else:
        return HttpResponse('This is a POST only endpoint!', status=405)