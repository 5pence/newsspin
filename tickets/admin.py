from django.contrib import admin
from .models import Ticket, Vote


admin.site.register(Ticket)
admin.site.register(Vote)
