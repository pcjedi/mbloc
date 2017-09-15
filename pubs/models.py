from django.db import models

class Search_string(models.Model):
    searchstring = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    trigger_counter = models.PositiveIntegerField()
