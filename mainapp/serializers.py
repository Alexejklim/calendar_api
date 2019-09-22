from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from holydays.models import CountrysList
from mainapp.models import Event, REMIND_CHOICES


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )


class EventSerializers(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Event
        fields = (
            'user',
            'event_name',
            'startdatetime',
            'enddatetime',
            'remind_in',)


class EventPostSerializers(serializers.ModelSerializer):
    enddatetime = serializers.DateTimeField(required=False)
    remind_in = serializers.ChoiceField(choices=REMIND_CHOICES, required=False)

    class Meta:
        model = Event
        fields = (
            'event_name',
            'startdatetime',
            'enddatetime',
            'remind_in',)


class MyRegisterSerializer(RegisterSerializer):
    country = serializers.CharField(max_length=30, required=False)

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'country': self.validated_data.get('country', '')
        }

    def save_usercountry(self, user):
        usercountry = user.usercountry
        usercountry.country = self.cleaned_data.get('country')
        if CountrysList.objects.filter(country=usercountry.country).exists():
            usercountry.save()
        elif usercountry.country:
            raise ValidationError("This country is not exist")
        return user

    def save(self, request):
        user = super(MyRegisterSerializer, self).save(request)
        self.save_usercountry(user)
        return user
