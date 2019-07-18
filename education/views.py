from django.shortcuts import render
# Create your views here.
def education_index(request):
    return render(request, 'education/index.html')

def comp_sci(request):
    return render(request, 'education/comp_sci.html')

def cog_sci(request):
    return render(request, 'education/cog_sci.html')

def class_history(request):
    return render(request, 'education/class_history.html')

def tech_dets(request):
    return render(request, 'education/tech_dets.html')
