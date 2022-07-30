from pyexpat import model
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Label(models.Model):
    label = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    explaination = models.TextField(max_length=500)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("labels_detail", kwargs={"pk": self.pk})
    

class Bin(models.Model):
    room = models.CharField(max_length=100)
    shelving_unit = models.CharField(max_length=100)
    shape = models.CharField(max_length=100)
    size = models.CharField(max_length=100)

    labels = models.ManyToManyField(Label)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.size} {self.shape}"
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"bin_id": self.id})
    

class Pen(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    number_owned = models.IntegerField()

    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.color} {self.brand}"
