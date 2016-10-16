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
    hashsum = models.CharField(max_length=512, blank=True, null=True)

    @staticmethod
    def send_project(player_ids, project):
        for id in player_ids:
            player = Player.get_by_id(id)
            player.project = project
            player.save()

    def set(self, arg):
        Player(**arg).save()

    @classmethod    
    def delete_by_id(cls, player_id):
        cls.objects.filter(pk=player_id).delete()
    
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, player_id):
        try:
            return cls.objects.get(id=player_id)
        except:
            return None
    

