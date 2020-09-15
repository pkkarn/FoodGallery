from django.shortcuts import render
from .models import *
from .filters import FoodFilter


def food_index(request):
    contents = Content.objects.all()
    cats = Category.objects.all()
    myFilter = FoodFilter(request.GET, queryset=contents)
    contents = myFilter.qs
    context = {
        'contents': contents,
        'cats': cats,
        'myFilter': myFilter,
    }
    return render(request, 'food/food_index.html', context)


def food_cat(request, pk):
    category = Category.objects.get(id=pk)
    contents = Content.objects.filter(category=category)
    cats = Category.objects.all()
    context = {
        'category': category,
        'cats': cats,
        'contents': contents,
    }
    return render(request, 'food/food_index.html', context)
