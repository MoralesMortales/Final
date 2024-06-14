from .views import mainView
from django.urls import path
urlpatterns = [
    path("", mainView, name="main")
]
