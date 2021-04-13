"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perpustakaan.views import buku, penerbit, tambahBuku, tambahKategori, ubahBuku 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'), # buku/ --> urlnya, buku --> view/method
    path('penerbit/', penerbit),
    path('tambah/buku/', tambahBuku, name='tambah_buku'),
    path('tambah/kategori/', tambahKategori, name='tambah_kategori'),
    path('buku/ubah/<int:id_buku>', ubahBuku, name='ubah_buku'), # urlnya dikasih name biar kalau mau ada ubah pola url, di views dan templatenya gausah diganti
]
