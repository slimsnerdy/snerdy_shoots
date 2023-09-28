# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  #new
from django.core.management.base import BaseCommand
from environs import Env

env = Env()
env.read_env()

class Command(BaseCommand):
    help = 'Creates a superuser.'
    
    def handle(self, *args, **options):
        User = get_user_model() #new
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser( 
                username=env.str('DB_USER'),
                password=env.str('DB_PASSWORD'),
                email=env.str('DB_EMAIL')  #new
            )
        print('Superuser has been created.')



# https://stackoverflow.com/a/26091252/1064843
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#django.contrib.auth.get_user_model


# #STEPS
# 1. delete all migrations folders manually
# 2. DROP all tables in database manually ONE BY ONE_OR_MORE
# 3. run makemigrations accounts, then run migrate
# 4. run createsuperuser
    # + below in 01-django.config file COMMENT out after migrations DONE
        #  03_superuser:
        #    command: "source /var/app/venv/*/bin/activate && python3 manage.py createsu"
        #    leader_only: true
    #REMEMBER TO COMMENT BACK ON AFTER SUPERUSER CREATED (ONE TIME USE COMMAND)