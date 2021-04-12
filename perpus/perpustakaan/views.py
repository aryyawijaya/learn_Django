from django.shortcuts import render

def buku(request):
    # subtitute variable
    judul = [
        'Belajar Django', 
        'Belajar REST API', 
        'Belajar Cara Belajar'
    ]
    penulis = 'Tom Cruise'
    
    konteks = {
        'title' : judul,
        'writer' : penulis
    }
    return render(request, 'buku.html', konteks)
def penerbit(request):
    return render(request, 'penerbit.html')