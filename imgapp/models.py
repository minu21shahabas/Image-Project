from django.db import models

# Create your models here.
class imgtable(models.Model):
    product=models.CharField(max_length=255)
    price=models.IntegerField()
    images=models.ImageField(upload_to="image/",null=True)