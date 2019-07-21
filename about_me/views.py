from django.shortcuts import render
# Create your views here.
def about_me_index(request):
    return render(request, 'about_me/index.html')

def hobbies(request):
    return render(request, 'about_me/hobbies.html')

def programming(request):
    return render(request, 'about_me/programming.html')

def leader(request):
    return render(request, 'about_me/leader.html')

def tech_dets(request):
    return render(request, 'about_me/tech_dets.html')
