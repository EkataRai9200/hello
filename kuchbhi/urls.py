
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms

class MyForm(forms.Form):
    username =forms.CharField(max_length=12)
    password = forms.CharField(max_length=100)



def form_views(request):
    data={
        'x':100
    }
    return render(request,'index.html', data)
def dash_board(request):
    data={

    }
    return render(request,'dash.html', data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",form_views),
    path("dash/",dash_board),
]
