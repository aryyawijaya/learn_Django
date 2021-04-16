from perpustakaan.models import Buku, Kategori
from rest_framework import serializers


class BukuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'

class KategoriSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'