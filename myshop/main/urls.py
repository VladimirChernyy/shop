from django.urls import path
from . import views

urlpatterns = [
    path('',views.catalog, name='catalog'),
    path('about',views.about, name='about'),
    path('create',views.create, name='create'),
    path('manual_tile_сutter',views.manual_tile_cutter, name='manual_tile_сutter'),
    path('electric_tile_cutter',views.electric_tile_cutter, name='electric_tile_cutter'),
    path('XL_size',views.XL_size, name='XL_size'),
]
