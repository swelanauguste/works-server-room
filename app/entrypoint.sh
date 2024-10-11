#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput
# python manage.py collectstatic --noinput
# python manage.py racks_stacks
# python manage.py switches
# python manage.py vlans
# python manage.py aruba
# python manage.py cisco
# python manage.py avaya11
# python manage.py avaya12
# python manage.py avaya21
# python manage.py avaya22

exec "$@"