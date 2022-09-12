from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
    'list': data_barang_catalog,
    'nama': 'Syafri Barry Salim',
    'npm' : '2106752136'
    }
    return render(request, "katalog.html", context)
