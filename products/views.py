from django.shortcuts import render
from django.http import HttpResponse
from . models import Product

from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    products = Product.__class__.objects.all()
    return render(request, 'index.html', {'products': products})


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "register.html"
