# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-d5dseb*l_$6!uw^y0zdzdv8&lazwn#l()&45@nojxana%76+z-'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'registration_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}

