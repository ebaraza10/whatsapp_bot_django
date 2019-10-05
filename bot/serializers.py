from rest_framework import serializers

from bot.models import Reminder


class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateField(required=False, allow_null=True)
    details = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = Reminder
        fields = ('date', 'details')

        