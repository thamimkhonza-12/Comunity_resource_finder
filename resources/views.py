from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Resource
from .serializers import ResourceSerializer
from .utils import haversine_distance

from rest_framework.decorators import action
from rest_framework.response import Response
from .utils import haversine_distance

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

    @action(detail=False, methods=['get'])
    def nearby(self, request):
        try:
            user_lat = float(request.query_params.get('lat'))
            user_lng = float(request.query_params.get('lng'))
            radius = float(request.query_params.get('radius', 10))
        except (TypeError, ValueError):
            return Response({"error": "Invalid or missing parameters"}, status=400)

        nearby_resources = []

        for resource in Resource.objects.select_related('location').all():
            loc = resource.location

            distance = haversine_distance(
                user_lat, user_lng,
                loc.latitude, loc.longitude
            )

            if distance <= radius:
                data = ResourceSerializer(resource).data
                data['distance_km'] = round(distance, 2)
                nearby_resources.append(data)

        return Response(nearby_resources)