from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'productApp/index.html')

def electronics(request):
    product_dict={
        'product1': 'MAC',
        'product2': 'IPhone',
        'product3': 'Dell',
    }
    return render(request, 'productApp/products.html', product_dict)

def toys(request):
    product_dict={
        'product1': 'Remote Car',
        'product2': 'Drone',
        'product3': 'Bambie',
    }
    return render(request, 'productApp/products.html', product_dict)

def shoes(request):
    product_dict={
        'product1': 'Nike',
        'product2': 'Addidas',
        'product3': 'Reebok',
    }
    return render(request, 'productApp/products.html', product_dict)