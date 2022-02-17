
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('<int:year>/<str:month>', views.home, name="home"),
    path('', include('Events.urls')),
]
