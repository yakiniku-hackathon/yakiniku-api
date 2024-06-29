from django.db import models


class Vps(models.Model):
    id = models.AutoField(verbose_name='項番', primary_key=True)
    vps_name = models.CharField(verbose_name='VPSのLocation Name', max_length=255, unique=True)
    title = models.CharField(verbose_name='画面に表示するタイトル', max_length=255, unique=True)
    file_name = models.CharField(verbose_name='GLBとpngのファイル名', max_length=255, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

class Model(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    title = models.CharField(verbose_name='画面に表示するタイトル', max_length=255, unique=True)
    file_name = models.CharField(verbose_name='GLBとpngのファイル名', max_length=255, unique=True)
    actions = models.TextField(verbose_name='glbのアクションの種類', null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)