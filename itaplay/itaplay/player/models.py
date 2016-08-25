from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    mac_address = models.CharField(max_length=17)
    status = models.BooleanField(default=False)

    def set(self, arg):
        self = Player(**arg)
        self.save()

    def delete(self):
        self.delete()
    
    @classmethod    
    def delete_by_id(cls, player_id):
        # player = cls.objects.get(id)
        # if player:
        #     player.delete()
        cls.objects.filter(pk=player_id).delete()
    @classmethod
    def get_all(cls):
        """
        return all players
        """
        return cls.objects.all()

    @classmethod
    def get_by_id(cls, player_id):
        return cls.objects.get(id=player_id)
