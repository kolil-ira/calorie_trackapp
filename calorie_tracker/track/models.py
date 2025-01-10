from django.db import models
from django.utils.timezone import now

class FoodEntry(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date = models.DateField(default=now)

    def __str__(self):
        return f"{self.name} - {self.calories} kcal"
