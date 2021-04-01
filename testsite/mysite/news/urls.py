from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('', views.index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    ]