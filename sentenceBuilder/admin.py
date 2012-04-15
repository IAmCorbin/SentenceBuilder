from sentenceBuilder.models import Word, Tag, Sentence
from django.contrib import admin
from django.contrib.auth.models import User

class WordAdmin(admin.ModelAdmin):
  list_display = ['name']
  fields = ['name', 'user']
admin.site.register(Word, WordAdmin)


class TagAdmin(admin.ModelAdmin):
  list_display = ['name']
  fields = ['name','words','user']
admin.site.register(Tag, TagAdmin)

admin.site.register(Sentence)
