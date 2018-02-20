DOCKER_PATH = registry.gitlab.com/gitlab-org/app
DOCKER_TAG = latest

.PHONY: docker-build
docker-build:
	docker build -t $(DOCKER_PATH):$(DOCKER_TAG) .

.PHONY: docker-run
docker-run:
	docker run -it --rm -p 8000:8000 $(DOCKER_PATH):$(DOCKER_TAG)

.PHONY: docker-rm-images
docker-rm-images:
	docker rmi $(shell docker images -f "dangling=true" -q)

.PHONY: docker-rm-containers
docker-rm-containers:
	docker rm -f $(shell docker ps -a -q)

.PHONY: pip-install
pip-install:
	pip install -r requirements.txt

.PHONY: lint
lint:
	flake8

.PHONY: migrate
migrate:
	./manage.py migrate

.PHONY: migrations
migrations:
	./manage.py makemigrations

.PHONY: pre-commit-flake
pre-commit-flake:
	flake8 --install-hook git && git config --bool flake8.strict true

.PHONY: run
run:
	./manage.py runserver 0.0.0.0:8000 --settings=my_site.settings.local

.PHONY: static
static:
	./manage.py collectstatic

.PHONY: test
test:
	pytest -vv
