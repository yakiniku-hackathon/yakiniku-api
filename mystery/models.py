import os
import uuid

from django.db import models

from users.models import User


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('images/', new_filename)


class Mystery(models.Model):

    STATUS_CHOICE = (
        (0, '下書き'),
        (1, '申請中'),
        (2, '公開中')
    )

    id = models.AutoField(verbose_name='項番', primary_key=True)
    title = models.CharField(verbose_name='謎解きのタイトル', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    image = models.ImageField(upload_to=upload_to, verbose_name='謎解きのサムネイル', null=True , blank=True)
    status = models.IntegerField(verbose_name='ステータス', choices=STATUS_CHOICE)
    mystery = models.TextField(verbose_name='問題文の番号', null=True , blank=True)
    complete_msg = models.TextField(verbose_name='完了メッセージ', null=True , blank=True)
    complete_count = models.IntegerField(verbose_name='謎解きをクリアされた回数', default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    published_at = models.DateTimeField(verbose_name='公開日時', null=True , blank=True)

    def __str__(self, ):
        return '【{}】{}'.format(self.status, self.title)

class Question(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    title = models.CharField(verbose_name='問題文のタイトル', max_length=255)
    description = models.TextField(verbose_name='問題文の詳細')
    hint = models.TextField(verbose_name='問題文のヒント', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    mystery = models.ForeignKey(Mystery, on_delete=models.CASCADE, verbose_name='謎解きID')
    correct_msg = models.TextField(verbose_name='正解時のメッセージ', null=True, blank=True)
    correct_vps = models.TextField(verbose_name='正解時のVPS', null=True, blank=True)
    correct_model = models.TextField(verbose_name='正解時に出現するモデル', null=True, blank=True)
    correct_game = models.TextField(verbose_name='正解時に出現するゲーム', null=True, blank=True)
    correct_msg_attributes = models.TextField(verbose_name='正解時のメッセージのattribute', null=True, blank=True)
    correct_vps_attributes = models.TextField(verbose_name='正解時のVPSのattribute', null=True, blank=True)
    correct_model_attributes = models.TextField(verbose_name='正解時に出現するモデルのattributes', null=True, blank=True)
    correct_game_attributes = models.TextField(verbose_name='正解時に出現するゲームのattributes', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    
    def __str__(self, ):
        return '{}'.format(self.title)
    
class UserMysteryStatus(models.Model):
    id = models.AutoField(verbose_name='項番', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='ユーザーID')
    mystery = models.ForeignKey(Mystery, on_delete=models.CASCADE, verbose_name='謎解きID')
    status = models.TextField(verbose_name='ユーザの謎解きのステータス', null=True, blank=True)

    def __str__(self, ):
        return '{}, {}'.format(self.user, self.mystery)