from django.urls import path,  include
from .views import signup , login
urlpatterns = [
    path("login/" , login , name='login'),
    path('signup/' , signup  , name='signup'),

]