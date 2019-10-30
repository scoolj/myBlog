from django.urls import path
from . import views, settings


urlpatterns = [
            path('',views.post_list, name='post_list'),
]