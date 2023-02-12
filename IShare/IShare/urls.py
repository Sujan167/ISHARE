from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from django.conf import settings
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
    path('accounts/', include('allauth.urls')),

]

handler404 = 'App.views.error404_template'
