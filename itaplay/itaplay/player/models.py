from __future__ import unicode_literals

from projects.models import AdviserProject
from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    mac_address = models.CharField(max_length=17)
    status = models.BooleanField(default=False)
    project = models.ForeignKey(AdviserProject, blank = True, null = True, on_delete=models.SET_NULL)

    def set(self, arg):
        self = Player(**arg)
        self.save()

    def delete(self):
        self.delete()
    
    @classmethod    
    def delete_by_id(cls, player_id):
        cls.objects.filter(pk=player_id).delete()
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, player_id):
        return cls.objects.get(id=player_id)
