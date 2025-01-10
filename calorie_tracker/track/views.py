from django.shortcuts import render, redirect
from .models import FoodEntry

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        calories = request.POST['calories']
        FoodEntry.objects.create(name=name, calories=calories)
        return redirect('home')

    entries = FoodEntry.objects.all().order_by('-date')
    total_calories = sum(entry.calories for entry in entries)
    return render(request, 'home.html', {'entries': entries, 'total_calories': total_calories})
