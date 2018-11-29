from django.urls import path
from . import views


# namespacing urls
app_name = 'music'

urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    # /register/
    path('register/', views.UserFormView.as_view(), name='register'),

    # /music/1/
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/1/
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/1/delete/
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]
