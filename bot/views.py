from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import (
     authentication_classes, 
     permission_classes
    )

from bot.serializers import ReminderSerializer
from bot.models import Reminder

from bot.handlers import (
        RemindersHandler,
    )


@authentication_classes([])
@permission_classes([])
class ReminderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

    @csrf_exempt
    def post(self, request):

        print(request.data)

        serializer = ReminderSerializer(data=request.data)

        if serializer.is_valid():
            # serializer.save()

            handler = RemindersHandler(request.data)
            handler.set_twilio_data()
            response_msg = handler.get_response()
            # return Response(
            #     data=serializer.data, 
            #     status=status.HTTP_201_CREATED
            # )
            return HttpResponse(response_msg)
        else:
            return Response(
                data={'message': serializer.errors}, 
                status=status.HTTP_400_BAD_REQUEST
            )







