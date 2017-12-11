.PHONY: lint run migrations migrate pre-commit-flake
lint:
	flake8

run:
	./manage.py runserver --settings=my_site.settings.local

migrations:
	./manage.py makemigrations

migrate:
	./manage.py migrate

pre-commit-flake:
	flake8 --install-hook git && git config --bool flake8.strict true
