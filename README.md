## Django REST Framework Tutorial

[Tutorial Link](http://www.django-rest-framework.org/tutorial/1-serialization "Tutorial Link")

- Tutorial 1: Serialization.
- Tutorial 2: Requests and Responses.
	- [The Browsable API](http://www.django-rest-framework.org/topics/browsable-api "The Browsable API")
- Tutorial 3: Class Based Views.
- Tutorial 4: Authentication and Permissions.
- Tutorial 5: Relationships and hyperlinked APIs
- Tutorial 6: Viewsets and Routers.

## Setup The Project

	virtualenv venv
	source venv/bin/activate
	pip install -r requirements.txt
	cd tutorial
	python manage.py runserver

## Development Notes
- To view the app, navigate to:
		
		localhost:8000 (will 404 before Tutorial #5)
		localhost:8000/admin/
		localhost:8000/snippets/

- How to delete the DB and start fresh:
		
		rm tmp.db
		python manage.py syncdb		
		Then, post a new snippet (see below)

- How to POST a snippet to the API:

		python manage.py runserver
		curl -X POST http://127.0.0.1:8000/snippets/ -d "code=print 789" -u user:password

- How to migrate the db [South migrations included in Django 1.7 by default]:

		python manage.py syncdb (this will tell you whether to makemigrations + migrate)
		python manage.py makemigrations
		python manage.py migrate

- How to query the db: Use the ‘dbshell’ command, and ‘.schema’ command to view db tables:
	
		Python manage.py dbshell
		.schema snippets_snippet
		.quit
