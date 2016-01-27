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

MEDIA_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "media"))
STATIC_ROOT = os.path.expanduser(os.path.join("~/Sites", SITE_DOMAIN, "static"))
