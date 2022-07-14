from django.db import models

# Create your models here.
class todos(models.Model):
    id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=200)

