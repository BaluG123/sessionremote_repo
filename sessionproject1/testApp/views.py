from django.shortcuts import render
from testApp import forms

# Create your views here.
def name_view(request):
    form=forms.name()
    return render(request,'testApp/name.html',{'form':form})

def age_view(request):
    name=request.GET['name']
    request.session['name']=name
    form=forms.age()
    return render(request,'testApp/age.html',{'form':form})

def gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=forms.gf()
    return render(request,'testApp/gf.html',{'form':form})

def result(request):
    gfname=request.GET['gfname']
    request.session['gfname']=gfname
    return render(request,'testApp/results.html')
