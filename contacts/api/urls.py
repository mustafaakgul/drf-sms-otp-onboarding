from django.urls import path
from contacts.api.views import (
                            ContactCreateAPIView,
                            ContactListAPIView,
                        )

app_name = "contacts"


urlpatterns = [
    path('create', ContactCreateAPIView.as_view(), name='create'),
    path('list', ContactListAPIView.as_view(), name='list'),
]