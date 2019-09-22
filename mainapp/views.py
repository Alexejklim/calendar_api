from datetime import datetime, timedelta

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from mainapp.models import Event
from mainapp.tasks import send_notification_email
from mainapp.serializers import EventSerializers, EventPostSerializers


class BaseEvent(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get_response(events):
        serializer = EventSerializers(events, many=True)
        return Response({'data': serializer.data})


class EventsDay(BaseEvent):

    def get(self, request):
        events = Event.objects.filter(user=request.user,
                                      startdatetime__year=request.data['year']
                                      , startdatetime__month=request.data['month']
                                      , startdatetime__day=request.data['day'])
        return self.get_response(events)


class EventsMonth(BaseEvent):

    def get(self, request):
        events = Event.objects.filter(user=request.user,
                                      startdatetime__year=request.data['year']
                                      , startdatetime__month=request.data['month'])
        return self.get_response(events)


class Events(BaseEvent):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        events = Event.objects.filter(user=request.user)
        return self.get_response(events)

    def post(self, request):
        event = EventPostSerializers(data=request.data)
        if event.is_valid():
            if request.data['remind_in'] != '0':
                notification_time = datetime.strptime(request.data['startdatetime'], "%Y-%m-%dT%H:%M:%S.%f") - timedelta(hours=int(request.data['remind_in']))
                send_notification_email.apply_async((request.user.email, request.data), eta = notification_time )
            event.save(user=request.user)
            return Response({'status': "Add"})
        return Response({'status': "Error"})
