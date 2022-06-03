from django.shortcuts import render
from .models import CategoryModel

# Create your views here.
def order(request):
    if request.method == 'GET':
        return render(request, 'order.html')
    elif request.method == 'POST':
        coffee_category = request.POST.get('coffee_category', '')
        category = CategoryModel.objects.get(coffee_category)

        return render(request, 'order.html')

