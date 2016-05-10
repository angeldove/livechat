from __future__ import unicode_literals

from django.db import models


class Room(models.Model):
    """
    model for a chat room
    """
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(_('Active'), default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    
    def __unicode__(self):
        return self.name


class Message(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(User)
    receiver = models.ForeignKey(User)
    room = models.ForeignKey(Room)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    
    def __unicode__(self):
        return self.content[:30]
