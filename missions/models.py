from django.db import models
from cats.models import Cat
from django.core.exceptions import ValidationError

class Mission(models.Model):
    cat = models.OneToOneField(Cat, on_delete=models.SET_NULL, null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Mission for {self.cat.name if self.cat else 'Unassigned'}"

    def delete(self, *args, **kwargs):
        if self.cat:
            raise ValidationError("Cannot delete a mission assigned to a cat.")
        super().delete(*args, **kwargs)

class Target(models.Model):
    mission = models.ForeignKey(Mission, on_delete=models.CASCADE, related_name="targets")
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return f"Target: {self.name} ({self.country})"