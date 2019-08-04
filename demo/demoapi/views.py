from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response

from .models import (
    DemoModel
)
from .serializers import (
    DemoSerializer, AnotherSerializer
)


class OwnerPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class TestDemo:
    def __init__(self):
        self.field100 = True
        self.field200 = "omed"


class DemoViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = DemoSerializer

    lookup_field = 'field1'

    permission_classes = (permissions.IsAuthenticated, OwnerPermission)

    def get_queryset(self):

        user = self.request.user
        return DemoModel.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['get'], detail=True,
            url_path='demo', url_name='demo')
    def demo(self, request, field1=None):
        # normally do something with this
        self.get_object()
        # place data into this serializer
        d = AnotherSerializer(TestDemo()).data
        return Response(d)

    @action(methods=['get'], detail=True,
            url_path='demo2', url_name='demo2')
    def demo2(self, request, field1=None):
        # normally do something with this
        self.get_object()
        # place data into this serializer
        d = AnotherSerializer([TestDemo()], many=True).data
        return Response(d)
