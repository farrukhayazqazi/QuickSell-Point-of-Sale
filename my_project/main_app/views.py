from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'main_app/index.html')

def charts(request):
    return render(request,'main_app/charts.html')

def cards(request):
    return render(request,'main_app/cards.html')

def buttons(request):
    return render(request,'main_app/buttons.html')

def tables(request):
    return render(request,'main_app/tables.html')

def animation(request):
    return render(request,'main_app/utilities-animation.html')

def border(request):
    return render(request,'main_app/utilities-border.html')

def color(request):
    return render(request,'main_app/utilities-color.html')

def other(request):
    return render(request,'main_app/utilities-other.html')