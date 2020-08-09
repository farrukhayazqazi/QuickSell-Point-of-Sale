from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request,'base.html')


@login_required(login_url='accounts:login')
def index(request):
    return render(request,'main_app/index.html')

