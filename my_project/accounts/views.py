from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import SignUpForm

# Create your views here.



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_app:index')
    else:
        form = SignUpForm()
    return render(request,'accounts/signup.html',{'form':form})




    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)

    #     if form.is_valid():
    #         user = form.save()
    #         login(request,user)
    #         # log in the user
    #         return redirect('main_app:index')
    # else:
    #     form = UserCreationForm()
    # return render(request,'accounts/signup.html',{'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            # log in the user
            user = form.get_user()
            login(request,user)

            if 'next' in request.POST:
                return redirect(request.POST.get('next'))

            else:
                return redirect('main_app:index')

    else:
        form = AuthenticationForm()

    return render(request,'accounts/login.html',{'form':form})



def logout_view(request):

    if request:
        logout(request)
        return redirect('accounts:login')

