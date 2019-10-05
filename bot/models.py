import uuid
from model_utils.models import TimeStampedModel
from django.db import models


class BaseModel(TimeStampedModel):
    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
        )

    class Meta:
        abstract = True
        ordering = ['-modified']


class Reminder(TimeStampedModel):
    date = models.DateField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return '{} - {}'.format(
            self.date,
            self.details
        )
