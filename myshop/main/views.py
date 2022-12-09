from django.shortcuts import render
from django.http import HttpResponse

# all_urls = {
#     'catalog': 'main/catalog.html',
#     'about': 'main/about.html',
#     'create': 'main/create.html',
#     'manual_tile_сutter': 'main/manual_tile_сutter.html',
#     'electric_tile_cutter': 'main/electric_tile_cutter.html',
#     'XL_size': 'main/XL_size.html',
# }


def catalog(request):
    return render(request, 'main/catalog.html')


def grocery_basket(request):
    return render(request, 'main/grocery_basket.html')


def create(request):
    return render(request, 'main/create.html', )


def manual_tile_cutter(request):
    return render(request, 'main/manual_tile_сutter.html')


def electric_tile_cutter(request):
    return render(request, 'main/electric_tile_cutter.html')


def XL_size(request):
    return render(request, 'main/XL_size.html')
