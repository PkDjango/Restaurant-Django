from django.shortcuts import render, get_object_or_404
from .models import Category, MenuItem

# Create your views here.


def menu_list(request, category_slug=None):
    category = None
    menu = MenuItem.objects.all()
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        menu = menu.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'menu': menu,
    }

    return render(request, 'menu/list.html', context)


def menu_detail(request, id, slug):
    menu = get_object_or_404(MenuItem, id=id, slug=slug)
    context = {'menu': menu}
    return render(request, 'menu/detail.html', context)
