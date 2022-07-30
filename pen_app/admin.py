from django.contrib import admin
from .models import Bin, Pen, Label

# Register your models here.
admin.site.register(Bin)
admin.site.register(Pen)
admin.site.register(Label)