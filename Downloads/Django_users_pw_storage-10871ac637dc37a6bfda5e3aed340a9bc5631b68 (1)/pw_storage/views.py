from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.
from .forms import LoginForm, RegisterForm
from .models import User

def home_page(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    return render(request, 'pw_storage/home.html')

def register_page(request):
    user_form = RegisterForm()
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)   
        if user_form.is_valid():
            if User.objects.filter(username=user_form.cleaned_data['username']).count() or User.objects.filter(email=user_form.cleaned_data['email']).count() or User.objects.filter(full_name=user_form.cleaned_data['full_name']).count():
                 return render(request, home_page)
            else:
                new_user = User.objects.create_user(username=user_form.cleaned_data.get('username'), full_name=user_form.cleaned_data.get('full_name'), email=user_form.cleaned_data.get('email'),password=user_form.cleaned_data.get('password1'))
                new_user.save()
                user = authenticate(new_user)
                login(request, user)
                return redirect(reverse(home_page))
    context = {'form': user_form}
    return render(request, 'pw_storage/user_account/register.html', context)            


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.authenticate_user()
            print(user)
            if user is not None:
                print("FOUND")
            else:
                print("STILL NONE")
            # if User.objects.filter(username=form.cleaned_data.get('username')).count():
            #     if User.objects.filter(password=form.cleaned_data.get('password')).count():
            #         # user = User.objects.get(username=form.cleaned_data.get('username'))
            #         user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            #         print(user.objects.get(username=form.cleaned_data('username')))
            #         # login(request, user)
            #         print("FOUND USER")
            #         return redirect(user_pw_all)
            #     else:    
            #         request.session['invalid_user'] = 1 # 1 == True
            #         messages.warning(request, 'Please enter the right password!')
            # else:
            #     messages.warning(request, 'Please enter the right username or create a new account!')
    return render(request, "pw_storage/user_account/login.html", {"form": form})
    # if request.method == 'POST':
    #     if form.is_valid():
            
    #         user = authenticate(request, username=username, password=password)
    #         print(user)
    #         if user is not None:
    #             print(user)
    #             login(request, user)
    #             return redirect(user_pw_all)
  
@login_required(login_url=login_page)
def logged_out_page(request):
    logout(request)
    return render(request, "pw_storage/user_account/logged_out.html")
    
@login_required(login_url=login_page)
def user_pw_all(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    return render(request, "pw_storage/user_password/user_pw_all.html")

@login_required(login_url=login_page)
def user_pw_add(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    return render(request, "pw_storage/user_password/user_pw_add.html")

@login_required(login_url=login_page)
def user_pw_search(request):
    if request.user.is_authenticated:
        messages.success(request, "Logged in as %s" % request.user)
    return render(request, "pw_storage/user_password/user_pw_search.html")

