
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, 
        name="home"),
    path('Events',views.all_events, name="list-events"),
    path('Add_venue',views.Add_venue,name="add_venue"),
    path('list_venues',views.list_venues,name="list_venues"),
    path('show_venue/<venue_id>', views.show_venue,name='show-venue'),
    path('search_venues', views.search_venues, name = 'search-venues'),
     path('update_venue/<venue_id>', views.update_venue,name='update-venue'),
     path('Add_event',views.Add_event,name="add_event"),
     path('update_Event/<event_id>', views.update_Event,name='update-event'),
     path('delete_event/<event_id>',views.delete_event, name='delete-event'),
     path('delete_event/<event_id>', views.delete_event, name="delete-event"),
     path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
     path('venue_text',views.venue_text, name='venue-text'),
     path('venue-csv',views.venue_csv, name='venue-csv'),
     path('My_Events',views.My_Events, name='My_Events'),
     path('search_events',views.search_events, name='search_events'),
     path('admin_approval',views.admin_approval, name='admin_approval'),
]