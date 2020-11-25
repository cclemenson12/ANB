from contacts_proj.settings import *

DEBUG = True
ALLOWED_HOSTS = ['abafm.org', 'utild.abafm.org']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':'/var/opt/contacts_proj/contacts.db',
    }
}
STATIC_ROOT = '/var/cache/contacts_proj/static/'
STATIC_URL = '/static/'
MEDIA_ROOT = '/var/opt/contacts_proj/media/'
MEDIA_URL = '/media/'
