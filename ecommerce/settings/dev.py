from .base import *

# ALLOWED_HOSTS = ["lighting-portal-humancode.c9users.io", "lighting-portal-humancode.c9users.io"]
ALLOWED_HOSTS =["light-source-humancode.c9users.io"]
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')




EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

