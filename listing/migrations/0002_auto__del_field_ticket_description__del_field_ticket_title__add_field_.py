# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Ticket.description'
        db.delete_column('listing_ticket', 'description')

        # Deleting field 'Ticket.title'
        db.delete_column('listing_ticket', 'title')

        # Adding field 'Ticket.new_title'
        db.add_column('listing_ticket', 'new_title',
                      self.gf('django.db.models.fields.CharField')(default='empyt', max_length=50),
                      keep_default=False)

        # Adding field 'Ticket.new_description'
        db.add_column('listing_ticket', 'new_description',
                      self.gf('django.db.models.fields.CharField')(default='empty', max_length=500),
                      keep_default=False)

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ticket.description'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.description' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Ticket.title'
        raise RuntimeError("Cannot reverse this migration. 'Ticket.title' and its values cannot be restored.")
        # Deleting field 'Ticket.new_title'
        db.delete_column('listing_ticket', 'new_title')

        # Deleting field 'Ticket.new_description'
        db.delete_column('listing_ticket', 'new_description')

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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listing': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['listing.Listing']"}),
            'new_description': ('django.db.models.fields.CharField', [], {'default': "'empty'", 'max_length': '500'}),
            'new_title': ('django.db.models.fields.CharField', [], {'default': "'empyt'", 'max_length': '50'}),
            'ticket_quantity': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['listing']