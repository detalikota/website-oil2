from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'services'

    def __str__(self):
        return self.name
