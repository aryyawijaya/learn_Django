from perpustakaan.models import Buku, Kategori
from perpustakaan.serializers import BukuSerializer, KategoriSerializer
from rest_framework import viewsets, permissions

class BukuViewSet(viewsets.ModelViewSet):
    # endpoint, user dapat GET, dll
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    permission_classes = [permissions.IsAuthenticated]

class KategoriViewSet(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer