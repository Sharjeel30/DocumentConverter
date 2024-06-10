from django.urls import path
from . import views

app_name = 'converter'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),
    path('success/<int:pk>/', views.convert_success, name='convert_success'),
]
