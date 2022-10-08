from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
]