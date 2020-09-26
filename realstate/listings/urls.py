from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.listings_index, name='listings_index'),
    path('<int:listing_id>', views.listing_n, name='listing_n'),
    path('search/', views.search, name='search')
]
