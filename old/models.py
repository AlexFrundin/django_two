# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Laptop(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    screen = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'laptop'


class Pc(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    cd = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pc'


class Printer(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    color = models.CharField(max_length=1)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'printer'


class Product(models.Model):
    maker = models.CharField(max_length=10)
    model = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'product'
