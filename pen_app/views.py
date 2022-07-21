from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pen

class PenCreate(CreateView):
    model = Pen
    fields = '__all__'
    success_url = '/pens/'

class PenUpdate(UpdateView):
    model = Pen
    fields = ['number_owned',]

class PenDelete(DeleteView):
    model = Pen
    success_url = '/pens/'

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