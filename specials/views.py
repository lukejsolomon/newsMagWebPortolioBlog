from django.shortcuts import render
from .models import Outline


def home(request):
    outline = Outline.objects.all()
    return render(request, 'specials/home.html', {'outline': outline})
