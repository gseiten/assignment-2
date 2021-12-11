from django.shortcuts import render


def index(request):
    context = {
        'form_type': 'register'
    }
    return render(request, 'test_app/index.html', context)


def home(request):
    ''' After successfull login. '''
    return render(request, 'test_app/home.html')


def user(request):
    '''  Make edits to user  details. '''
    return render(request, 'test_app/user.html')


def company(request):
    '''  Make edits to company details. '''
    return render(request, 'test_app/company.html')
