from django.shortcuts import render

# Create your views here.
from .models import Emergency
#from .forms import EventModelForm
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

# class EmergencyCreate(LoginRequiredMixin, FormUserNeededMixin, CreateView):
#     form_class=EmergencyModelForm
#     template_name="emergency/create.html"
#     login_url=   reverse_lazy("admin:login")
#     success_url= reverse_lazy("emergency")

def home_view(request):
    return render(request,"emergency/home.html",{})


def add_contact(request):
	return render(request,"emergency/add-contact.html",{})

def added(request):
	return render(request,"emergency/added-contacts.html",{})