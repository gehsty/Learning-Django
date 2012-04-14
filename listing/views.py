from django.http import HttpResponse
from django.template import Context, loader
from listing.models import Listing, Ticket
from django.shortcuts import render_to_response

def index(request):
    upcoming_listings = Listing.objects.all().order_by('-gig_date')[:5]
    return render_to_response ('ticket/index.html', {'upcoming_listings': upcoming_listings})

def detail(request, listing_id):
    return HttpResponse("You're looking at listing %s." % listing_id)

