from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
  name = models.CharField(max_length=50)
  user = models.ForeignKey(User, related_name='+')
  def __unicode__(self):
    return self.name
    
class Tag(models.Model):
  name = models.CharField(max_length=70)
  words = models.ManyToManyField(Word, blank=True)
  user = models.ForeignKey(User, related_name='+')
  def __unicode__(self):
    return self.name
    
class Sentence(models.Model):
  name = models.CharField(max_length=70)
  words = models.ManyToManyField(Word)
  user = models.ForeignKey(User, related_name='+')
  def __unicode__(self):
    return self.name
    
class SentencePosition(models.Model):
  word = models.ForeignKey(Word)
  sentence = models.ForeignKey(Sentence)
  position = models.IntegerField()
