from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
# def demo(request):
#     return HttpResponse("my project")

# def demo(request):
    # if request.method=="POST":
    #     f_n=request.POST.get("fname")
    #     l_n=request.POST.get("lname")
#     return render(request,"forms.html")

def demo(request):
    post=Blog.objects.all()
    return render(request,"base.html",{'post':post})