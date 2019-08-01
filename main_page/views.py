from django.shortcuts import render
import subprocess



# Create your views here.
def index(request):
    r = subprocess.call("git log -1 --date=short --pretty=format:%cd", shell=True)
    print(r)
    return render(request, 'main_page/index.html')
