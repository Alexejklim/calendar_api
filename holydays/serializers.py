from rest_framework import serializers

from holydays.models import CountrysList, Holydays


class CountrysListPostSerializers(serializers.ModelSerializer):

    class Meta:
        model = CountrysList
        fields = (
            'country',)


class HolydaysSerializers(serializers.ModelSerializer):
    class Meta:
        model = Holydays
        fields = (
            'country',
            'event_name',
            'begin',
        )
