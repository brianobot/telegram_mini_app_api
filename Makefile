shell:
	python3 manage.py shell

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

run-local:
	python3 manage.py runserver

test-local:
	python3 -m pytest -s