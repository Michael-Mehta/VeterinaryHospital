# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Owners(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'owners'


class Vets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vets'


class Pets(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255, blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pets'


class Appointments(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(blank=True, null=True)
    pet = models.ForeignKey(Pets, models.DO_NOTHING, blank=True, null=True)
    vet = models.ForeignKey(Vets, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'appointments'



class Vaccines(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vaccines'


class PetVaccines(models.Model):
    id = models.BigAutoField(primary_key=True)
    pet = models.ForeignKey(Pets, models.DO_NOTHING, blank=True, null=True)
    vaccine = models.ForeignKey(Vaccines, models.DO_NOTHING, blank=True, null=True)
    time_of_vaccination = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pet_vaccines'
