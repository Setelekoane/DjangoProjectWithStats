
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, 
        name="home"),
    path('Events',views.all_events, name="list-events"),
    path('Add_venue',views.Add_venue,name="add_venue"),
    path('list_venues',views.list_venues,name="list-venues"),
    
]
