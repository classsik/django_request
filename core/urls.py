from django.contrib import admin
from django.urls import path, re_path

from main import views

urlpatterns = [
    path('', views.home),
    re_path(r'^user/(?P<login>\D+)/(?P<folder_name>\D+)/(?P<post_id>\d+)', views.user),
    re_path(r'^user/(?P<login>\D+)/(?P<folder_name>\D+)', views.user),
    re_path(r'^user/(?P<login>\D+)', views.user),
    re_path(r'^user', views.user),
    re_path(r'^error', views.error),
    path('admin/', admin.site.urls),
]
