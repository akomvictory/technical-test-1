from rest_framework import serializers
from .models import URLMapping

class URLMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapping
        fields = ['original_url', 'shortened_url']
