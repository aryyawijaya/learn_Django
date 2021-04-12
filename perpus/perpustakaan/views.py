from django.shortcuts import render

def buku(request):
    return render(request, 'buku.html')
def penerbit(request):
    return render(request, 'penerbit.html')