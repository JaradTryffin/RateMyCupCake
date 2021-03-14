from django.urls import path
from .views import add_cake,cake_detail,rate_cake



urlpatterns=[
    path('add/',add_cake,name='add_cake'),
    path('<int:cake_id>/',cake_detail,name='cake_detail'),
    path('<int:cake_id>/rate_cake/',rate_cake,name='rate_cake'),
]