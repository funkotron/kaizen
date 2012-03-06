# Create your views here.
from api.codebase import CodeBase
from tickets.models import Ticket, User, Status, Category

def get_tickets():
	cb = CodeBase()
	page=1
	try:
		while True:
			cb_tickets = cb.search("resolution:open&page=%d"%page)
			for cb_ticket in cb_tickets:
				ticket, created = Ticket.objects.get_or_create(number=cb_ticket.find('ticket-id').text)
				if cb_ticket.find('assignee').text:
					ticket.assignee, created = User.objects.get_or_create(name=cb_ticket.find('assignee').text)
				status_id = int(cb_ticket.find('status-id').text)
				status_name = cb_ticket.find('status').find('name').text
				ticket.status, created = Status.objects.get_or_create(number=status_id,defaults={'name':status_name})
				ticket.summary = cb_ticket.find('summary').text
				try:
					category_id = int(cb_ticket.find('category-id').text)
					category_name = cb_ticket.find('category').find('name').text
					ticket.category, created = Category.objects.get_or_create(number=category_id,defaults={'name':category_name})
				except:
					pass
				ticket.save()
			page += 1
	except:
		pass

