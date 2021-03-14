from django.urls import path,include

from .views  import dashboard,view_rating,view_dashboard_cake

urlpatterns=[
    path('',dashboard,name='dashboard'),
    path('cake/<int:cake_id>/',view_dashboard_cake,name='view_dashboard_cake'),
    path('rate/<int:rate_id>/',view_rating,name='view_rating'),
    
]