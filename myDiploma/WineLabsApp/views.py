from django.shortcuts import render
from .models import Wine
from django.core.paginator import Paginator


def index(request):
    sneak_peek_wines = Wine.objects.all()[:3]

    return render(request, 'index.html', {'sneak_peek_wines': sneak_peek_wines})

def db(request):
    gg = Wine.image

    return render(request,'db.html', {'gg': gg})



def wines(request):
    red_wines = Wine.objects.filter(type='Red')[:3]
    white_wines = Wine.objects.filter(type='White')[:3]
    sparkling_wines = Wine.objects.filter(type='Sparkling')[:3]

    context = {
        'red_wines': red_wines,
        'white_wines': white_wines,
        'sparkling_wines': sparkling_wines,
    }

    return render(request, 'wines.html', context)


def wines_page_red(request):
    red_wines_list = Wine.objects.filter(type='Red')
    paginator = Paginator(red_wines_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'red-wines.html', {'page_obj': page_obj})


def wines_page_white(request):
    white_wines_list = Wine.objects.filter(type='White')
    paginator = Paginator(white_wines_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'white-wines.html', {'page_obj': page_obj})


def wines_page_sparkling(request):
    sparkling_wines_list = Wine.objects.filter(type='Sparkling')
    paginator = Paginator(sparkling_wines_list, 9)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sparkling-wines.html', {'page_obj': page_obj})


def wines_all(request):
    all_wines = Wine.objects.all()

    # Get the selected keywords from the request
    selected_keywords = request.GET.getlist('keywords')

    # Filter wines based on selected keywords
    filtered_wines = all_wines
    for keyword in selected_keywords:
        filtered_wines = filtered_wines.filter(keywords__icontains=keyword)

    # Paginate the filtered wines
    paginator = Paginator(filtered_wines, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'test.html', {'page_obj': page_obj, 'selected_keywords': selected_keywords})


