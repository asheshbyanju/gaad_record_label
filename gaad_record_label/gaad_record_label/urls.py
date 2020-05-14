from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
path('admin/', admin.site.urls),
    path('', include('gaad_record_label.urls')),
    path('accounts/', include('accounts.urls'))
    path('', views.index, name="home"),
    path('artist/<int:artist_id>/', views.artist_details, name="artist_detail"),
    path('artist/', views.artist_list, name="artist_list")
]
