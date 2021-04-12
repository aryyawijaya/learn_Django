from django.contrib import admin
from perpustakaan.models import Buku, Kategori

# Register your models here.

class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul', 'penulis', 'kategori_id', 'jumlah'] # field yg akan ditampilkan
    search_fields = ['judul', 'penulis', 'penerbit'] # pencarian berdasar ini
    list_filter = ('kategori_id',)
    list_per_page = 4


admin.site.register(Buku, BukuAdmin)
admin.site.register(Kategori)