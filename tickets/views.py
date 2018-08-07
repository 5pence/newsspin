from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from .models import Ticket, Vote


def post_ticket_list(request):
    features = Ticket.objects.filter(created_date__lte=timezone.now(), ticket_type=Ticket.FEATURE).order_by('money_raised')
    bugs = Ticket.objects.filter(created_date__lte=timezone.now(), ticket_type=Ticket.BUG)
    vote_dict = {}
    if request.user:
        votes = Vote.objects.filter(user=request.user)
        for v in votes:
            vote_dict[v.ticket_id] = True
    bugs = [(b, b.id in vote_dict) for b in bugs]
    return render(request, 'tickets/ticket_list.html', {'features': features, 'bugs': bugs, 'votes': vote_dict})


def ticket_vote(request):
    bug = Ticket.objects.get(id=request.GET['id'])
    user = request.user
    vote = Vote(user=user, ticket=bug)
    vote.save()
    return HttpResponseRedirect(reverse('ticket_list'))
