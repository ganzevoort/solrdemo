from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.name

class CarModel(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer)
    price = models.IntegerField()
    milage = models.IntegerField()

    def __unicode__(self):
        return u'{} {}'.format(self.manufacturer.name, self.name)

