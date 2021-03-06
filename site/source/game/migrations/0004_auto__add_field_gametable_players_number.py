# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'GameTable.players_number'
        db.add_column(u'game_gametable', 'players_number',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'GameTable.players_number'
        db.delete_column(u'game_gametable', 'players_number')


    models = {
        u'game.gametable': {
            'Meta': {'object_name': 'GameTable'},
            'game_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'players_number': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'prev_state': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['game']