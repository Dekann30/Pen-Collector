from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bin, Label
from .forms import PenForm

class BinCreate(LoginRequiredMixin, CreateView):
    model = Bin
    fields = '__all__'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = '/bins/'

class BinUpdate(LoginRequiredMixin, UpdateView):
    model = Bin
    fields = ['room', 'shelving_unit']

class BinDelete(LoginRequiredMixin, DeleteView):
    model = Bin
    success_url = '/bins/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def bins_index(request):
    bins = Bin.objects.filter(user=request.user)
    return render(request, 'bins/index.html', { 'bins': bins })

@login_required
def bins_detail(request, bin_id):
    bin = Bin.objects.get(id = bin_id)
    labels_bin_doesnt_have = Label.objects.exclude(id__in = bin.labels.all().values_list('id'))  
    pen_form = PenForm()
    return render(request, 'bins/detail.html', {'bin': bin, 'pen_form': pen_form, 'labels': labels_bin_doesnt_have})

@login_required
def add_pen(request, bin_id):
    form = PenForm(request.POST)
    if form.is_valid():
        new_pen = form.save(commit=False)
        new_pen.bin_id = bin_id
        new_pen.save()
    return redirect('detail', bin_id=bin_id)

@login_required
def assoc_label(request, bin_id, label_id):
    Bin.objects.get(id=bin_id).labels.add(label_id)
    return redirect('detail', bin_id=bin_id)


class LabelList(LoginRequiredMixin, ListView):
    model = Label

class LabelDetail(LoginRequiredMixin, DetailView):
    model = Label

class LabelCreate(LoginRequiredMixin, CreateView):
    model = Label
    fields = '__all__'

class LabelUpdate(LoginRequiredMixin, UpdateView):
    model = Label
    fields = '__all__'

class LabelDelete(LoginRequiredMixin, DeleteView):
    model = Label
    success_url = '/labels/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)