from django.urls import path
from . import views

app_name = "cowryapp"

urlpatterns = [
    path('', views.CreateRandomUUIDAndReturnListAPIView.as_view())
]