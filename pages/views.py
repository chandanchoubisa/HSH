from django.shortcuts import render

from django.http import HttpResponse

from listings.models import Listing
from brokers.models import Broker
from listings.options import price_options,bedroom_options,state_options


def index(request):
	listings=Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

	context={
		'listings':listings,
		'price_options':price_options,
		'bedroom_options':bedroom_options,
		'state_options':state_options
	}
	return render(request,'pages/index.html',context)


def about(request):

	brokers=Broker.objects.order_by('-hire_date')

	mvp_brokers=Broker.objects.all().filter(is_mvp=True)

	context={
		'brokers':brokers,
		'mvp_brokers':mvp_brokers
	}
	return render(request,'pages/about.html',context)
# Create your views here.
