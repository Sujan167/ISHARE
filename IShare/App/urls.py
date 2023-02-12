from django.urls import path
# from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginpage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),


    path("error404_template/", views.error404_template, name="error404_template"),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('updatePost/<int:post_id>/', views.updatePost, name='updatePost'),
    path('commentPost/<int:post_id>/', views.commentPost, name='commentPost'),
    path('profile/', views.profile, name='profile'),
    path('roadmap/', views.roadmap, name='roadmap'),
    path('frequently/', views.frequently, name='frequently'),
    path('notification/', views.notification, name='notification'),
    path('challange/', views.challange, name='challange'),
    path('help/', views.help, name='help'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),

]
# urlpatterns = patterns('',
#     url(r'^dashboard/$', views.dashboard, name='dashboard'),
# )
