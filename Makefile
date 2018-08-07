
start:
	./wait-for-postgres.sh db
	shorten/manage.py migrate
	shorten/manage.py runserver 0.0.0.0:8000
