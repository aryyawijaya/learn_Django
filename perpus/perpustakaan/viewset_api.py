from perpustakaan.models import Buku
from perpustakaan.serializers import BukuSerializer
from rest_framework import viewsets, permissions

class BukuViewSet(viewsets.ModelViewSet):
    # endpoint, user dapat GET, dll
    queryset = Buku.objects.all()
    serializer_class = BukuSerializer
    permission_classes = [permissions.IsAuthenticated]