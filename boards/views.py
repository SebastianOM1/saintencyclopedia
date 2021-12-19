from django.http.request import HttpHeaders
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse, response

from .forms import NewSaintForm
from .models import Saint

def home(request):
    saints = Saint.objects.all()
    return render(request, 'home.html', {'saints': saints})

def saint_page(request, id):
    saint = get_object_or_404(Saint, id=id)
    image= saint.art.url
    return render(request, "saint.html", {'saint':saint, 'image':image})

def new_saint(request):
    user = User.objects.first()
    if request.method == 'POST':
        form = NewSaintForm(request.POST)
        if form.is_valid():
            saint = form.save(commit=False)
            saint.save()
            return redirect('saint_page', id=saint.id)
    else:
        form = NewSaintForm()
    return render(request, 'new_saint.html', {'form':form})