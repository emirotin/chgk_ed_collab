from django.db import models
from lib.py_etherpad import EtherpadLiteClient

ep_client = EtherpadLiteClient()

class Author(models.Model):
    user = models.ForeignKey('User')
    ep_id = models.CharField(max_length=250)

    def initials(self):
        return ''
