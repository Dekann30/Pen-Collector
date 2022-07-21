from django.db import models

# Create your models here.
class Pen(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    tip_width = models.CharField(max_length=100)
    tip_type = models.CharField(max_length=100)
    number_owned = models.IntegerField()

    def __str__(self):
        return self.brand

# pens = [
#     Pen('Bic', 'black', '.7mm', 'ball point'),
#     Pen('Staedtler', 'green', '.5mm', 'felt'),
#     Pen('Sharpie', 'blue', '.7mm', 'felt'),
# ]