from __future__ import unicode_literals

from django.db import models


class Room(models.Model):
    """
    model for a chat room
    """
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    active = models.BooleanField(_('Active'), default=False)
    
    def __unicode__(self):
        return self.name
