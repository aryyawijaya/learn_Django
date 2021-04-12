from django.db import models

# Create your models here.
class Buku(models.Model):
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)

    def __init__(self):
        return self.judul # yg direturn harus tipe data string