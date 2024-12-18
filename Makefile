shell:
	python3 manage.py shell

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

run-local:
	python3 manage.py runserver_plus --cert-file cert.pem --key-file key.pem

test-local:
	python3 -m pytest -s

collectstatic:
	python3 manage.py collectstatic

check-deployment:
	python3 manage.py check --deploy