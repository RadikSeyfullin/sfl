from django.db import models

class Catalog(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    def __str__(self):
        return self.title
