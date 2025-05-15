from django.urls import path
from .views import menu_list, menu_detail

app_name = 'menu'

urlpatterns = [
    path('', menu_list, name='menu_list'),
    path('<slug:category_slug>', menu_list, name='menu_list_by_category'),
    path('<int:id>/<slug:slug>', menu_detail, name='menu_detail'),
]
