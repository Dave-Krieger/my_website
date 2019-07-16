from django.shortcuts import render
# Create your views here.
def about_me_index(request):
    return render(request, 'about_me/index.html')

def comp_sci(request):
    return render(request, 'about_me/comp_sci.html')

def cog_sci(request):
    return render(request, 'about_me/cog_sci.html')

def tech_dets(request):
    return render(request, 'about_me/tech_dets.html')

def hobbies(request):
    return render(request, 'about_me/hobbies.html')

def class_history(request):
    return render(request, 'about_me/class_history.html')
