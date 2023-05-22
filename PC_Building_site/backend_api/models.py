from django.db import models


class Processor(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    frequency = models.IntegerField()
    socket = models.CharField()
    core_number = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class CoolingSystem(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    rotational_speed = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Motherboard(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    chipset = models.CharField()
    socket = models.CharField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class RAM(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    memory_type = models.CharField()
    clock_frequency = models.IntegerField()
    memory_size = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class Videocard(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    memory_size = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class HDD(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    memory_size = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class SSD(models.Model):
    objects = None
    name = models.CharField()
    firm = models.CharField()
    memory_size = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


class PowerUnit(models.Model):
    objects = None
    name = models.CharField()
    power = models.IntegerField()
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
