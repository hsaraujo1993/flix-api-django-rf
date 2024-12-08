from django.db import models

# Create your models here.

NATIONALITY_CHOICES = (('BR', 'Brazil'),
                       ('US', 'United States'))

class Actor(models.Model):
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(choices=NATIONALITY_CHOICES, max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

