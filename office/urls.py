from django.urls import path
from office import views #llamo a views para trabajar con las urls


urlpatterns = [
    path('', views.inicio, name="Inicio"), 

]