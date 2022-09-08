from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('users', views.create_user),
    # path('show', views.some_function), nisam siguran da li je ovo problem
    path('success', views.success),
]