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

def tech_dets(request):
    return render(request, 'data_viz/tech_dets.html')
