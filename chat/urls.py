from django.urls import path
from .views import join ,all , single
urlpatterns = [
    path('join/' , join , name="join") , 
    path('all/' ,all , name="all" )  , 
    path('id=<int:pk>/' ,single , name = "single" )

]