"""
Implement pagination and search in a Django application.
@ALBIN MAMMEN MATHEW
Roll No: 08 
Date: 20/02/2026
"""
from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Item

def item_list(request):
    query = request.GET.get('q', '')
    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        ).order_by('name')
    else:
        items = Item.objects.all().order_by('name')

    paginator = Paginator(items, 5) # Show 5 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'items_app/item_list.html', {
        'page_obj': page_obj,
        'query': query
    })
