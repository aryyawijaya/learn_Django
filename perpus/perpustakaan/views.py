from django.shortcuts import render
from perpustakaan.models import Buku

def buku(request):
    # subtitute variable
    books = Buku.objects.all() 
    # ORM (Object-Relational Mapping) --> mengambil model tampa query sql
    
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