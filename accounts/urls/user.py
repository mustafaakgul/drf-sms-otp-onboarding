from django.urls import include, path
from rest_framework.routers import DefaultRouter

from ..views import UserViewsets

app_name = 'accounts'

router = DefaultRouter()
router.register('', UserViewsets)

urlpatterns = [
    path('', include(router.urls)),
]