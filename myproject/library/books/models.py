from django.db import models

# Create your models here.
class Book(models.Model):
    tittle=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    price=models.IntegerField()
    pdf=models.FileField(upload_to="book/pdf")
    cover=models.ImageField(upload_to="book/images",null=True,blank=True)
    def __str__(self):
        return self.tittle

