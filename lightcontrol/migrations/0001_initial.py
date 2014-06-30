# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Remote'
        db.create_table(u'lightcontrol_remote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('identifier', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'lightcontrol', ['Remote'])

        # Adding model 'Device'
        db.create_table(u'lightcontrol_device', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('identifier', self.gf('django.db.models.fields.IntegerField')()),
            ('remote', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lightcontrol.Remote'])),
        ))
        db.send_create_signal(u'lightcontrol', ['Device'])


    def backwards(self, orm):
        # Deleting model 'Remote'
        db.delete_table(u'lightcontrol_remote')

        # Deleting model 'Device'
        db.delete_table(u'lightcontrol_device')


    models = {
        u'lightcontrol.device': {
            'Meta': {'object_name': 'Device'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'remote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['lightcontrol.Remote']"})
        },
        u'lightcontrol.remote': {
            'Meta': {'object_name': 'Remote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.BigIntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['lightcontrol']