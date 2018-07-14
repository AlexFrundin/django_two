from django.db import models


class Laptop(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    screen = models.SmallIntegerField()


class Pc(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    speed = models.SmallIntegerField()
    ram = models.SmallIntegerField()
    hd = models.FloatField()
    cd = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

class Printer(models.Model):
    code = models.IntegerField(primary_key=True)
    model = models.ForeignKey('Product', models.DO_NOTHING, db_column='model')
    color = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)


class Product(models.Model):
    maker = models.CharField(max_length=10)
    model = models.CharField(primary_key=True, max_length=50)
    type = models.CharField(max_length=50)
