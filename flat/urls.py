from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views, models

urlpatterns = [
    path('',views.home,name='home'),
    path('flats/', views.search, name='search'),
    path('flats/<int:id>/', views.FlatDetailView.as_view(), name='flat_detail'),
    path('add_flat/', views.FlatAddView.as_view(), name='add'),
    path('flats/<int:id>/update/', views.FlatUpdateView.as_view(), name='update'),
    path('flats/<int:id>/delete/', views.FlatDeleteView.as_view(), name='delete'),
    path('accounts/', include('django.contrib.auth.urls')),

]
