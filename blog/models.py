from django.db import models
from accounts.models import CustomUser

class Blog(models.Model):

    class Meta:
        db_table = 'blog'

    user = models.ForeignKey(CustomUser, verbose_name='作成者', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    content = models.TextField(verbose_name='内容')
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    def __str__(self):
        return self.title
