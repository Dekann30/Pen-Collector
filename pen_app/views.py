from django.shortcuts import render
from .models import Pen

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pens_index(request):
    pens = Pen.objects.all()
    return render(request, 'pens/index.html', { 'pens': pens })

def pens_detail(request, pen_id):
    pen = Pen.objects.get(id = pen_id)
    return render(request, 'pens/detail.html', {'pen': pen})