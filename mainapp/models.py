from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

REMIND_CHOICES = (
    (0, 'not_remind'),
    (1, 'one_hour'),
    (2, 'two_hours'),
    (4, 'four_hours'),
    (24, 'day'),
    (168, 'week'),)


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(verbose_name='Event', max_length=80)
    startdatetime = models.DateTimeField(verbose_name='Start datetime')
    enddatetime = models.DateTimeField(verbose_name='End datetime', blank=True)
    remind_in = models.IntegerField(verbose_name='Remind in', choices=REMIND_CHOICES, default=0)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        if not self.enddatetime:
            self.enddatetime = datetime(self.startdatetime.year
                                        , self.startdatetime.month
                                        , self.startdatetime.day
                                        , 23, 59, 59)
        super(Event, self).save(*args, **kwargs)

    class Meta:
        ordering = ('startdatetime',)
        verbose_name = 'Event',


class UserCountry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.CharField(verbose_name='Country', max_length=30, blank=True)


@receiver(post_save, sender=User)
def create_user_country(sender, instance, created, **kwargs):
    if created:
        UserCountry.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_country(sender, instance, **kwargs):
    instance.usercountry.save()
