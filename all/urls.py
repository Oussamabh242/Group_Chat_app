from django.urls import path,  include
from .views import wellcome
urlpatterns = [
    path("" ,wellcome , name="wellcome" )
]