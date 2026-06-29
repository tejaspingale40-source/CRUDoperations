from django.urls import path
from .views import *

urlpatterns = [
   
path('index/',index_view),
path('create/',create_view),
path('display/',display_view),
path('update/<str:n>/',update_view),
path('delete/<str:n>/',delete_view),
path('register/',register_view),
path('login/',login_view),

]