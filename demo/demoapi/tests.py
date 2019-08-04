from collections import OrderedDict

from django.contrib.auth.models import User
from django.test import TestCase

from rest_framework.test import APIRequestFactory

from .models import DemoModel

from .views import DemoViewSet


# Create your tests here.
class TestGenerate(TestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        # create a user
        self.user = User.objects.create_user('demotest', 'demotest@demo.demo', '123456789q.')
        self.demo = DemoModel(user=self.user, field1="thisonetest", field2=True)
        self.demo.save()

    def test_demo(self):
        request = self.factory.get('/demo/thisonetest/demo/', '', content_type='application/json')
        request.user = self.user
        my_view = DemoViewSet.as_view(actions={
            'get': 'demo',
        })

        response = my_view(request, field1='thisonetest')

        assert response.status_code == 200
        assert response.data == {'field100': True, 'field200': 'omed'}

    def test_demo2(self):
        request = self.factory.get('/demo/thisonetest/demo2/', '', content_type='application/json')
        request.user = self.user
        my_view = DemoViewSet.as_view(actions={
            'get': 'demo2'
        })

        response = my_view(request, field1='thisonetest')

        assert response.status_code == 200
        assert response.data == [OrderedDict([('field100', True), ('field200', 'omed')])]
