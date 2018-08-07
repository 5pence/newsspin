from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_ticket_list, name='ticket_list'),
    path('vote', views.ticket_vote, name='ticket_vote'),
]
