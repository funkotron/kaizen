from tickets.models import Ticket, User, Status
from django.http import HttpResponse
from django.conf import settings
from django.core.context_processors import csrf
from kaizen.djangojinja2 import render_to_response, render_to_string
from tickets.helpers import get_tickets
from tickets.forms import UpdateTicketForm

def whiteboard(request, *args, **kwargs):
	"""The default whiteboard view"""
	context = {}
	context['tickets'] = Ticket.objects.all()
	context['users'] = User.objects.all()
	statuses = Status.objects.all()
	#'New' in ordering makes it very long
	ordering = getattr(settings,'STATUS_ORDERING')
	context['statuses'] = [statuses.get(name=ordered_name) for ordered_name in ordering]
	context['ticket_url_prefix'] = getattr(settings,'TICKET_URL_PREFIX')
	template = 'whiteboard.html'
	return render_to_response(template,context,request)

def whiteboard_min(request, *args, **kwargs):
	return whiteboard(request, condensed=True, *args, **kwargs)

def refresh(request, *args, **kwargs):
	"""Update the local tickets"""
	get_tickets()
	return whiteboard(request)

def modal(request, ticket_no=None, *args, **kwargs):
	"""Return a modal dialog via AJAX"""
	context = {}
	ticket = Ticket.objects.get(number=ticket_no)
	if request.method == 'POST':
		form = UpdateTicketForm(request.POST, instance=ticket)
		if form.is_valid():
			form.save()
			return HttpResponse('OK')
	else:
		form = UpdateTicketForm(instance=ticket)
	context['form'] = form
	context['ticket'] = ticket
	context['users'] = User.objects.all()
	context.update(csrf(request))
	template = 'modal.html'
	return HttpResponse(render_to_string(template,context=context,request=request))

def status_update(request, ticket_no=None, status_id=None, *args, **kwargs):
	"""Update the status by dragging a ticket across columns"""
	ticket = Ticket.objects.get(number=ticket_no)
	status = Status.objects.get(id=status_id)
	ticket.status = status
	ticket.save()
	return HttpResponse()
