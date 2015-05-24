import json

from django.db import models


# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=128)
    cities = models.ManyToManyField('City')

    @property
    def get_cities(self):
        return [city.__json__() for city in self.cities.all()]

    def __unicode__(self):
        return self.name

    def __json__(self):
        return {
            'country_name': self.name,
            'cities': self.get_cities
        }

        return json.dumps(data)


class City(models.Model):
    name = models.CharField(max_length=128)
    streets = models.ManyToManyField('Street')

    @property
    def get_streets(self):
        return [street.__json__() for street in self.streets.all()]

    def __unicode__(self):
        return self.name

    def __json__(self):
        return {
            'city_name': self.name,
            'streets': self.get_streets
        }


class Street(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name

    def __json__(self):
        return self.name
