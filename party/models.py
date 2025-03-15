import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    party_date = models.DateField()
    party_time = models.TimeField()
    invitation = models.TextField()
    venue = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "parties"

    def __str__(self):
        return f"{self.venue}, {self.party_date}"


class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)  # noqa: DJ01
    party = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.gift


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE, related_name="guests")

    def __str__(self):
        return str(self.name)
