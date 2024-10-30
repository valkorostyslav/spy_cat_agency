from django.db import models
import requests


# Create your models here.

def get_cat_breeds():
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds")
        response.raise_for_status()
        
        breeds = response.json()
        
        return [(breed['name'], breed['name']) for breed in breeds if 'name' in breed]
    except requests.RequestException:
        return [
            ('Siberian', 'Siberian'),
            ('Persian', 'Persian'),
            ('British Shorthair', 'British Shorthair'),
        ]

class Cat(models.Model):
    BREEDS = get_cat_breeds()
    
    name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()
    breed = models.CharField(max_length=50, choices=BREEDS)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.breed})"