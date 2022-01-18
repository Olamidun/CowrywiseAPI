from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import RandomUUID
from .serializers import RandomUUIDSerializer
from datetime import datetime


# Create your views here.
class ListAndCreateModelMixin:
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        random_uuid = RandomUUID.objects.create(timestamp=datetime.now())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CreateRandomUUIDAndReturnListAPIView(generics.ListAPIView):
    serializer_class = RandomUUIDSerializer
    def get_queryset(self):
        context = {}
        RandomUUID.objects.create(timestamp=datetime.now())
        random_uuids = RandomUUID.objects.all().order_by('-timestamp')
        return random_uuids
        # for uuid in random_uuids:
        #     context[uuid.timestamp] = uuid.id
        #     print(context)
        #     return random_uuids
            
        # print(context)