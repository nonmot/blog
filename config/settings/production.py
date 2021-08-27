from .common import *
import dj_database_url

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', 'https://slovephys.com', env('ALLOWED_HOST')]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUDINARY_NAME': 'hm3adoj0t',
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_SECRET')
}

CORS_ORIGIN_WHITELIST = [
    'https://lovephys.com',
]

CORS_ALLOW_HEADERS = (
    'access-control-allow-origin',
)

CORS_ALLOW_CREDENTIALS = True

# 静的ファイルを配置する場所
STATIC_ROOT = '/usr/share/nginx/html/static'
MEDIA_ROOT = '/usr/share/nginx/html/media'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
