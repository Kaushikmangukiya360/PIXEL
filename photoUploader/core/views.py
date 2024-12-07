from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method == "POST":
        form = imgForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
    form = imgForm
    img = imgData.objects.all()
    return render(request, 'index.html', {'imgForm' : form, 'img': img})

def delete(request, id):
    d = imgData.objects.get(id=id)
    d.delete()
    return redirect('/')

def update(request, id):
    img = imgData.objects.all()
    return render(request, 'update.html', {'id': id, 'img': img})