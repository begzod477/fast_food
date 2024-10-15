from django.urls import path
from .views import create_food , update_food
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<int:category_id>/', views.select_by_category, name='select_by_category'),
    path('create/', create_food, name='create_food'),
    path('update/<int:id>/', update_food, name='update_food'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)