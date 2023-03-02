from rest_framework import serializers
from .models import CatMed

class CatSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CatMed
        fields = ['id', 'cat_name', 'age', 'breed']

