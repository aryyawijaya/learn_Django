from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama = models.CharField(max_length=9)
    keterangan = models.TextField

    def __str__(self):
        return self.nama


class Buku(models.Model):
    # django auto bikin primary key berupa field id
    judul = models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    kelompok_id = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    # on_delete=models.CASDCADE --> misal jika kategori masak dihapus maka semua buku dengan kategori masak akan terhapus juga

    def __init__(self):
        return self.judul # yg direturn harus tipe data string