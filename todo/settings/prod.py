from .base import * 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
