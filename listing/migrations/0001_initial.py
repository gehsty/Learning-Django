# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Listing'
        db.create_table('listing_listing', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('band', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('gig_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('location_town', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('location_venue', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('listing', ['Listing'])

        # Adding model 'Ticket'
        db.create_table('listing_ticket', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('listing', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listing.Listing'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('ticket_quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('delivery', self.gf('django.db.models.fields.CharField')(max_length=2)),
        ))
        db.send_create_signal('listing', ['Ticket'])

    def backwards(self, orm):
        # Deleting model 'Listing'
        db.delete_table('listing_listing')

        # Deleting model 'Ticket'
        db.delete_table('listing_ticket')

    models = {
        'listing.listing': {
            'Meta': {'object_name': 'Listing'},
            'band': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gig_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_town': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'location_venue': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'listing.ticket': {
            'Meta': {'object_name': 'Ticket'},
            'delivery': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['listing.Listing']"}),
            'ticket_quantity': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['listing']