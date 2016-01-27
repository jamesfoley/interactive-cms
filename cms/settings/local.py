from base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "interactive-cms",
        "USER": os.getlogin(),
        "PASSWORD": "",
        "HOST": "",
        "PORT": ""
    }
}
