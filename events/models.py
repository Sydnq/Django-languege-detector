from django.db import models
from django.urls import reverse


class Event(models.Model):
    detected_languege = models.CharField(max_length=200)
    query_text = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.detected_languege

    def get_absolute_url(self):
        return reverse('events:detail', args=[self.id])
