from django.db import models
from django.utils import timezone
from users.models import User


class Ticket(models.Model):
    TODO = 'todo'
    DOING = 'doing'
    DONE = 'done'
    BUG = 'bug'
    FEATURE = 'feature'
    TICKET_STATUS_CHOICES = (
        (TODO, 'todo'),
        (DOING, 'doing'),
        (DONE, 'done')
    )
    TICKET_TYPE_CHOICES = (
        (BUG, 'bug'),
        (FEATURE, 'feature')
    )
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    completed_date = models.DateTimeField(
            blank=True, null=True)
    ticket_status = models.CharField(max_length=5, choices=TICKET_STATUS_CHOICES, default=TODO)
    ticket_type = models.CharField(max_length=7, choices=TICKET_TYPE_CHOICES, default=FEATURE)
    up_vote = models.IntegerField(null=True, blank=True)
    money_raised = models.IntegerField(null=True, blank=True)
