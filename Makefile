up-db:
	docker-compose -f docker-compose-pg.yaml up

# Flask
up-flask-w-4:
	gunicorn -w=4 --bind 0.0.0.0:5000 Servers.Flask.server:app --timeout 120
up-flask-w-12:
	gunicorn -w=12 --bind 0.0.0.0:5000 Servers.Flask.server:app --timeout 120
up-flask-w-13:
	gunicorn -w=13 --bind 0.0.0.0:5000 Servers.Flask.server:app --timeout 120
# FasAPI
up-fastapi-w-4:
	#uvicorn Servers.FastAPI.server:app --host 0.0.0.0 --port 5001 --log-level critical
	gunicorn Servers.FastAPI.server:app --workers 4  \
				--worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5001

up-fastapi-w-12:
	gunicorn Servers.FastAPI.server:app --workers 12 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5001
up-fastapi-w-13:
	gunicorn Servers.FastAPI.server:app --workers 13 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5001

# Django
up-django-orm-w-4:
	cd 'Servers/Django/Django&ORM'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5002 --workers 4

up-django-orm-w-12:
	cd 'Servers/Django/Django&ORM'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5002 --workers 12

up-django-orm-w-13:
	cd 'Servers/Django/Django&ORM'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5002 --workers 13

# Django without ORM
up-django-w-4:
	cd 'Servers/Django/Django&Psycopg2'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5003 --workers 4

up-django-w-12:
	cd 'Servers/Django/Django&Psycopg2'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5003 --workers 12

up-django-w-13:
	cd 'Servers/Django/Django&Psycopg2'; \
	gunicorn speed_test.wsgi:application --bind 0.0.0.0:5003 --workers 13


# http asyncpg
up-aiohttp-w-4:
	gunicorn Servers.Aiohttp.server:app --workers 4 --worker-class aiohttp.GunicornWebWorker --bind 0.0.0.0:5005
up-aiohttp-w-12:
	gunicorn Servers.Aiohttp.server:app --workers 12 --worker-class aiohttp.GunicornWebWorker --bind 0.0.0.0:5005
up-aiohttp-w-13:
	gunicorn Servers.Aiohttp.server:app --workers 13 --worker-class aiohttp.GunicornWebWorker --bind 0.0.0.0:5005

# blacksheep
up-sheep-w-4:
	gunicorn Servers.BlackSheep.server:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5006
up-sheep-w-12:
	gunicorn Servers.BlackSheep.server:app --workers 12 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5006
up-sheep-w-13:
	gunicorn Servers.BlackSheep.server:app --workers 13 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5006

up-sanic-gn-w-4:
	gunicorn Servers.Sanic.server:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5007
up-sanic-gn-w-12:
	gunicorn Servers.Sanic.server:app --workers 12 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5007
up-sanic-gn-w-13:
	gunicorn Servers.Sanic.server:app --workers 13 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5007

up-sanic-w-4:
	sanic Servers.Sanic.server:app --host=0.0.0.0 --port=5007 --no-motd --workers=4
up-sanic-w-12:
	sanic Servers.Sanic.server:app  --host=0.0.0.0 --port=5007 --no-motd --workers=12
up-sanic-w-13:
	sanic Servers.Sanic.server:app  --host=0.0.0.0 --port=5007 --no-motd --workers=13
