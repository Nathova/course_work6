SECRET_KEY = 'django-insecure-@akpd##p)(1!^oc3f_vt*=!cgrl)2l9xbst42@j@l@4jguc54l'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WSGI_APPLICATION = 'config.wsgi.application'

SUPERUSER_NAME = 'Admin Adminov'
SUPERUSER_PASSWORD = 'pbkdf2_sha256$600000$j3AhUodRE7gyxh791LamBn$0upmRM1difoZ6iFgytkA6+uTUhF4oPn3c1RXnr8et4c='

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yandex.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('YANDEX_PASSWORD_APP')
