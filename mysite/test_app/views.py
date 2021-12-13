from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import UserForm, UserUpdateForm, CompanyUpdateForm


def login(request):

    print("HIT")
    if request.user.is_authenticated:
        return redirect('home')

    return render(request, 'test_app/login.html')


def register(request):
    ''' Register new users.
    '''

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created! You are now able to login.')
            return redirect('login')
    else:
        form = UserForm()

    context = {
        'form_type': 'register',
        'form': form
    }
    return render(request, 'test_app/register.html', context)


@login_required
def home(request):
    ''' Displays user and company details of the authenticating user.
    '''

    context = {
        'user_details': request.user,
        'company_details': Company.objects.filter(employee=request.user).first()
    }
    return render(request, 'test_app/home.html', context)


@login_required
def user(request):
    ''' Updates user details.
    '''

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been updated!')
            return redirect('home')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'test_app/user.html', context)


@login_required
def company(request):
    ''' Reads and Updates Company details for user.
    '''

    user_company = Company.objects.filter(employee=request.user).first()

    if request.method == 'POST':
        form = CompanyUpdateForm(request.POST, instance=user_company)
        if form.is_valid():
            form.instance.employee = request.user
            form.save()
            messages.success(
                request, f'Your Company details have been updated!')
            return redirect('home')
    else:
        form = CompanyUpdateForm(instance=user_company)

    context = {
        'form': form
    }
    return render(request, 'test_app/company.html', context)
