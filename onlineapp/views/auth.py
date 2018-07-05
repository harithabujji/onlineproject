
from django.views import View

from django.shortcuts import *
import ipdb
from django.views.generic import *
from django import forms
from onlineapp.forms import *
from django.urls import *
from django.contrib.messages import constants as messages
from django.contrib.messages.constants import *
from django.contrib import messages
from django.contrib.auth.models import *

from django.contrib.auth import *


class SignupController(View):

    def get(self, request):
        pass
        form=Signupform()
        return render(
            request,
            template_name='onlineapp/signup.html',
            context={
                'form':form,'title':'login'
            }
        )

    def post(self,request):
        pass
        form=Signupform(request.POST)
        if form.is_valid():
            user=User.objects.create_user(**form.cleaned_data)
            user.save()
            user=authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"]
            )

        if user is not None:
            login(request,user)
            return redirect('onlineapp:colleges')
        else:
            messages.error(request,"invaalid Credentials")

        return render(
            request,
            template_name='onlineapp:colleges',
            context={

            }
        )


class LoginController(View):
    def get(self,request,*args,**kargs):
        login =  Loginform()
        return render(
            request,
            template_name="onlineapp/login.html",
            context={'form':login,'title':'Login Form'}
        )

    def post(self, request, *args, **kwargs):
        form = Loginform(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user is not None:
                login(request,user)
                return redirect('onlineapp:college_html')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('onlineapp:login')

def logout_user(request):
    logout(request)
    return redirect('onlineapp:login')