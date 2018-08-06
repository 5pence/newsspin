from django.db import models
from django.utils import timezone
from tickets.models import Ticket


class Transaction(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
