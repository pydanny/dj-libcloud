DEBUG=True
USE_TZ=True
DATABASES={
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}
ROOT_URLCONF="djlibcloud.urls"
INSTALLED_APPS=[
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "djlibcloud",
]
SITE_ID=1
STATIC_URL = '/files/'
STATICFILES_STORAGE = 'djlibcloud.storage.LibCloudStorage'
SECRET_KEY = 'TESTSECRET'

LIBCLOUD_PROVIDERS = {
    'local': {
        'type': 'libcloud.storage.types.Provider.LOCAL',
    },
}
DEFAULT_LIBCLOUD_PROVIDER = 'local'