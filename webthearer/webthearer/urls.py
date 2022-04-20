

from django.urls import path

from webthearer.webthearer import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/', views.movie, name='movies')
]
