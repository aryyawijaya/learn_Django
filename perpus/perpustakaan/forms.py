from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku, Kategori

class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__' # semua field yg ada di model Buku uang akan ditampilkan di form input
        # ['judul', 'penulis'] --> hanya field tertentu yg muncul
        # exlude = ['judul'] --> semua field muncul kecuali judul

        widgets = {
            'judul': forms.TextInput({'class':'form-control'}),
            'penulis': forms.TextInput({'class':'form-control'}),
            'penerbit': forms.TextInput({'class':'form-control'}),
            'jumlah': forms.NumberInput({'class':'form-control'}),
            'kategori_id': forms.Select({'class':'form-control'}),

        }

class FormKategori(ModelForm):
    class Meta:
        model = Kategori
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'keterangan':forms.Textarea({'class':'form-control'}),
        }