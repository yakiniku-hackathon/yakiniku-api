from django.db import models


class HealthCheck(models.Model):

    id = models.AutoField(verbose_name='項番', primary_key=True)
    data = models.CharField(verbose_name='ヘルスチェック', max_length=4)
