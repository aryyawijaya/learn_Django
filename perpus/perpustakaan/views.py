from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku, FormKategori

def buku(request):
    # subtitute variable
    books = Buku.objects.all()
    # ORM (Object-Relational Mapping) --> mengambil model tampa query sql

    # FILTER table

    # select * form Buku where penerbit=Gramedia
    # books = Buku.objects.filter(penerbit='Gramedia')

    # filter pakai foreign key
    # books = Buku.objects.filter(kategori_id__nama='Novel') # inner join di django (ORM)

    # limit data yang ditampilkan
    # books = Buku.objects.filter()[:3]
    
    konteks = {
        'Buku' : books
    }
    return render(request, 'buku.html', konteks)
def penerbit(request):
    books = Buku.objects.all()

    konteks = {
        'Buku' : books
    }
    return render(request, 'penerbit.html', konteks)

# client --> urls --> view --> model --> view --> templates --> client

def tambahBuku(request):
    if request.POST: # jika ada data yg dikirim menggunakan method POST maka
        form = FormBuku(request.POST) # form dengan data inputan
        if form.is_valid(): # cek validasi inputan user/client
            form.save() # menyimpan data inputan ke database
            form = FormBuku()

            pesan = 'Data berhasil disimpan'

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-buku.html', konteks)
    else: # jika tidak
        form = FormBuku() # buat form kosong langsung render ke template tambah-buku.html

        konteks = {
            'form' : form,
        }
    return render(request, 'tambah-buku.html', konteks)

def tambahKategori(request):
    if request.POST:
        form = FormKategori(request.POST)
        if form.is_valid():
            form.save()
            form = FormKategori()

            pesan = 'Data berhasil disimpan'

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-kategori.html', konteks)
    else:
        form = FormKategori()

        konteks = {
            'form': form,
        }
        return render(request, 'tambah-kategori.html', konteks)