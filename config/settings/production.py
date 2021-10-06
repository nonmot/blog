from .common import *
import dj_database_url

SECRET_KEY = env('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com', 'lovephys.com', env('ALLOWED_HOST')]

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

DEFAULT_FILE_STORAGE = 'config.backends.MediaStorage'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')


STATICFILES_STORAGES = 'storages.backends.s3boto3.S3Boto3Storage'
STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'


CORS_ALLOWED_ORIGINS = [
    'https://lovephys.com',
]

CORS_ALLOW_CREDENTIALS = True

# # 静的ファイルを配置する場所
# STATIC_ROOT = '/usr/share/nginx/html/static'
# MEDIA_ROOT = '/usr/share/nginx/html/media'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        # blogアプリケーションが利用するロガー
        'diary': {
            'handlers': ['file'],
        }
    },

    # ハンドラーの設定
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D', # ログローテーション（新しいファイルへの切り替え）間隔の単位
            'interval': 1, # ログローテーション間隔（1日）
            'backupCount': 7, # 保存しておくログファイル数
        }
    },

    # フォーマッタの設定
    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        }
    }
}
