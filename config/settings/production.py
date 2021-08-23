from config.settings.local import CORS_ORIGIN_ALLOW_ALL, CORS_ORIGIN_WHITELIST
from .common import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', 'netlify.app']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUDINARY_NAME': 'hm3adoj0t',
    'API_KEY': os.environ.get('API_KEY'),
    'API_SECRET': os.environ.get('API_SECRET')
}

CORS_ORIGIN_WHITELIST = (
    'https://jovial-gates-acd3c5.netlify.app'
)
