.PHONY: lint run makemigrations migrate
lint:
	flake8

run:
	./manage.py runserver --settings=my_site.settings.local

makemigrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate
