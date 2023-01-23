from django.shortcuts import render
from main.models import Product
from django.http import HttpResponseRedirect

# Create your views here.
def main(request):
    product = Product.objects.all()
    return render(request, 'index.html', {'product':product})