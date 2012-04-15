from listing.models import Listing, Ticket
from django.contrib import admin

class ListingAdmin(admin.ModelAdmin):
	fieldsets = [ 
		('Band Name',		{'fields': ['band']}), 
		('Gig Details',		{'fields': ['gig_date', 'location_town', 'location_venue']})
		]

admin.site.register(Listing, ListingAdmin)
admin.site.register(Ticket)