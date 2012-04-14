from django.db import models

# Create your models here.


class Listing(models.Model):
	band = models.CharField(max_length=50)
	gig_date = models.DateTimeField('Gig Date')
	location_town =  models.CharField(max_length=50)
	location_venue =  models.CharField(max_length=100)
	def __unicode__(self):
		return self.band

class Ticket(models.Model):
	DELIVERY_CHOICES = (
		('PO', 'Post to Buyer'),
		('CO', 'Buyer to collect at Venue'),
		('BO', 'The buyer is to post the tickets by pigeon' 
		)

	listing = models.ForeignKey(Listing)
	new_title = models.CharField(max_length=50, default = '')
	new_description = models.CharField(max_length=500, default = '')
	ticket_quantity = models.IntegerField()
	delivery = models.CharField(max_length=2, choices= DELIVERY_CHOICES)
	def __unicode__(self):
		return self.new_title
