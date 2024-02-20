from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import URLMapping
from .serializers import URLMappingSerializer
import hashlib

@api_view(['POST'])
def shorten_url(request):
    if request.method == 'POST':
        original_url = request.data.get('original_url')
        if original_url:
            hash_object = hashlib.sha1(original_url.encode())
            short_url = hash_object.hexdigest()[:8]  # You can adjust the length of the shortened URL as needed
            try:
                url_mapping = URLMapping.objects.create(original_url=original_url, shortened_url=short_url)
            except:
                return Response({'error': 'Failed to create short URL.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = URLMappingSerializer(url_mapping)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Original URL is required.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def resolve_short_url(request, short_url):
    if request.method == 'GET':
        try:
            url_mapping = URLMapping.objects.get(shortened_url=short_url)
        except URLMapping.DoesNotExist:
            return Response({'error': 'Shortened URL does not exist.'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'original_url': url_mapping.original_url}, status=status.HTTP_200_OK)
