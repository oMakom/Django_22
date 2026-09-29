from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    latest_products = Product.objects.order_by('-created_at')[:5]
    print(latest_products)
    return render(request, 'home.html')

def contacts(request):
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Здесь мы возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contacts.html')
