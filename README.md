KAIZEN
======

Install:

* pip install -E requirements.pip
* Add CodeBase API settings to settings
* Run `./manage.py collectstatic`
* Run server `./manage.py runserver`
* Visit `/refresh` to pull tickets from CodeBase
* Visit `/` to view your new Kaizen board

Todo:

* Push changes on Ticket.save()
* AJAX refresh on modal update
* Assign categories colours
* Add websockets UI with django-socketio
* New ticket button next to logo
* Use activity feed
* Impelemt @all and released buttons
* Add settings page
