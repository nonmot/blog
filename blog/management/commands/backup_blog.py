import csv
import datetime
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Blog

class Command(BaseCommand):
    help = "Backup blog data"

    def handle(self, *args, **options):
        # 実行時のYYYMMDDを取得
        date = datetime.date.today().strftime("%Y%m%d")

        # 保存ファイルの相対パス
        file_path = settings.BACKUP_PATH + 'diary_' + date + '.csv'

        # 保存ディレクトリが存在しなければ作成
        os.makedirs(settings.BACKUP_PATH, exist_ok=True)

        # バックアップファイルの作成
        with open(file_path, 'w') as file:
            writer = csv.writer(file)

            # ヘッダーの書き込み
            header = [field.name for field in Blog._meta.fields]
            writer.writerow(header)

            # Blogテーブルの全データを取得
            blogs = Blog.objects.all()

            # データ部分の書き込み
            for blog in blogs:
                writer.writerow([blog.id,
                                str(blog.user),
                                blog.title,
                                blog.content,
                                blog.category.all(),
                                str(blog.created_at),
                                str(blog.updated_at)])
            
            # 保存ディレクトリのファイルパスを取得
            files = os.listdir(settings.BACKUP_PATH)
            # ファイルが設定数以上あったら一番古いファイルを削除
            if len(files) >= settings.NUM_SAVED_BACKUP:
                files.sort()
                os.remove(settings.BACKUP_PATH + file[0])