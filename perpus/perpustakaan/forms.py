from django.forms import ModelForm
from perpustakaan.models import Buku, Kategori

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__' # semua field yg ada di model Buku uang akan ditampilkan di form input
        # ['judul', 'penulis'] --> hanya field tertentu yg muncul
        # exlude = ['judul'] --> semua field muncul kecuali judul

class FormKategori(ModelForm):
    class Meta:
        model = Kategori
        fields = '__all__'