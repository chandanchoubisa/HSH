from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .options import price_options,bedroom_options,state_options

from .models import Listing
# Create your views here.
def index(request):
	listings=Listing.objects.order_by('-list_date').filter(is_published=True)
	paginator=Paginator(listings,6)

	page=request.GET.get('page')
	paged_listings=paginator.get_page(page)

	context={
		"listings":paged_listings
	}
	return render(request,'listings/listings.html',context)

def listing(request,listing_id):
	listing=get_object_or_404(Listing,pk=listing_id)

	context={
		'listing':listing
	}
	return render(request,'listings/listing.html',context)

def search(request):
	query_set_data=Listing.objects.order_by('-list_date')

	if 'keywords' in request.GET:
		keywords=request.GET['keywords']
		if keywords:
			query_set_data=query_set_data.filter(description__icontains=keywords)

	if 'city' in request.GET:
		city=request.GET['city']
		if city:
			query_set_data=query_set_data.filter(city__iexact=city)

	if 'state' in request.GET:
		state=request.GET['state']
		if state:
			query_set_data=query_set_data.filter(state__iexact=state)

	if 'bedrooms' in request.GET:
		bedrooms=request.GET['bedrooms']
		if bedrooms:
			query_set_data=query_set_data.filter(bedrooms__lte=bedrooms)

	if 'price' in request.GET:
		price=request.GET['price']
		if price:
			query_set_data=query_set_data.filter(price__lte=price)



	context={

		'price_options':price_options,
		'bedroom_options':bedroom_options,
		'state_options':state_options,
		'listings':query_set_data,
		'values':request.GET
	}
	return render(request,'listings/search.html',context)