from django.http import HttpResponse


def home_page(request):
    print('Home page Requested')
    return  HttpResponse('It is in Home page')