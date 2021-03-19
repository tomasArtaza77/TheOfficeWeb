from django.urls import path
from office import views #llamo a views para trabajar con las urls
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('', views.inicio, name="Inicio"), 

]

urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 