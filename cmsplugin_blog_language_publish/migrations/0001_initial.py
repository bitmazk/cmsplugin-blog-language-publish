# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EntryLanguagePublish'
        db.create_table('cmsplugin_blog_language_publish_entrylanguagepublish', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(related_name='published_languages', to=orm['cmsplugin_blog.Entry'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('pubished', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('cmsplugin_blog_language_publish', ['EntryLanguagePublish'])

        # Adding unique constraint on 'EntryLanguagePublish', fields ['entry', 'language']
        db.create_unique('cmsplugin_blog_language_publish_entrylanguagepublish', ['entry_id', 'language'])


    def backwards(self, orm):
        # Removing unique constraint on 'EntryLanguagePublish', fields ['entry', 'language']
        db.delete_unique('cmsplugin_blog_language_publish_entrylanguagepublish', ['entry_id', 'language'])

        # Deleting model 'EntryLanguagePublish'
        db.delete_table('cmsplugin_blog_language_publish_entrylanguagepublish')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_blog.entry': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Entry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'cmsplugin_blog_language_publish.entrylanguagepublish': {
            'Meta': {'unique_together': "(('entry', 'language'),)", 'object_name': 'EntryLanguagePublish'},
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'published_languages'", 'to': "orm['cmsplugin_blog.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'pubished': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['cmsplugin_blog_language_publish']
