from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import HttpResponse
from listings.models import listing


# Create your views here.
def listings_index(request):
    listings_list = listing.objects.all()

    paginator = Paginator(listings_list, 2)
    page = request.GET.get('page', 1)
    try:
        listings_list = paginator.page(page)
    except PageNotAnInteger:
        listings_list = paginator.page(1)
    except EmptyPage:
        listings_list = paginator.page(paginator.num_pages)

    context = {
        'listings_list': listings_list
    }
    return render(request, 'listings/listings.html', context)


def listing_n(request, listing_id):
    listing1 = listing.objects.get(id=listing_id)
    context = {
        'listing1': listing1
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    return render(request, 'listings/search.html')
