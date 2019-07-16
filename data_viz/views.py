from django.shortcuts import render
# Create your views here.
def data_viz_index(request):
    return render(request, 'data_viz/index.html')

def temperature(request):
    return render(request, 'data_viz/temperature.html')

def co2(request):
    return render(request, 'data_viz/co2.html')

def data_wrangle(request):
    return render(request, 'data_viz/data_wrangle.html')

def about_me(request):
    return render(request, 'data_viz/about_me.html')
