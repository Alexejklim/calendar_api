from django.db import models


class CountrysList(models.Model):
    country = models.CharField(verbose_name='Countrys', max_length=30, blank=False, unique=True)


class Holydays(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.CharField(verbose_name='Countrys', max_length=30, blank=True)
    event_name = models.CharField(verbose_name='Event', max_length=80)
    begin = models.DateTimeField(verbose_name='Begin datetime', blank=True, null=True)
