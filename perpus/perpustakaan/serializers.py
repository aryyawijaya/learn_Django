from perpustakaan.models import Buku
from rest_framework import serializers

class BukuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buku
        fields = '__all__'