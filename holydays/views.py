from django.db.utils import IntegrityError
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from holydays.holydaysparser import get_countrys, get_holydayevents
from holydays.models import CountrysList, Holydays
from holydays.serializers import CountrysListPostSerializers, HolydaysSerializers


class CountrysListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        countrys = CountrysList.objects.all()
        serializer = CountrysListPostSerializers(countrys, many=True)
        return Response({"data": serializer.data})


class HolydaysAdmin(APIView):
    permission_classes = [permissions.IsAdminUser]

    def save_holyday(self, country):
        for item in get_holydayevents(country):
            holyday = Holydays()
            holyday.country = country
            holyday.event_name = item[0]
            holyday.begin = item[1]
            holyday.save()

    def post(self, request):
        CountrysList.objects.all().delete()
        Holydays.objects.all().delete()
        for country in get_countrys():
            countryslist = CountrysList()
            countryslist.country = country
            try:
                countryslist.save()
            except IntegrityError:
                self.save_holyday(country)
            else:
                self.save_holyday(country)
        if countryslist:
            return Response({'status': "Done"})
        return Response({'status': "Error"})


class Holyday(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if request.user.usercountry.country:
            holydays = Holydays.objects.filter(country=request.user.usercountry.country,
                                               begin__year=request.data['year']
                                               , begin__month=request.data['month']
                                               )
            serializer = HolydaysSerializers(holydays, many=True)
            return Response({'data': serializer.data})
        return Response({'status': "Error - User has no country"})
