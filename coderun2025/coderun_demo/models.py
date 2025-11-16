from django.db import models

# Create your models here.
class Fruit(models.Model):
    name = models.CharField()
    weight = models.FloatField(default=0.0)
    color = models.CharField(default='red')

    def __str__(self):
        return f"(name={self.name}, color={self.color},weight={self.weight})"

