from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin

from .models import Mystery, Question, UserMysteryStatus


class MysteryResource(resources.ModelResource):
    class Meta:
        model = Mystery

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question

class UserMysteryStatusResource(resources.ModelResource):
    class Meta:
        model = UserMysteryStatus


@admin.register(Mystery)
class MysteryAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = MysteryResource

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = QuestionResource

@admin.register(UserMysteryStatus)
class UserMysteryStatusAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = UserMysteryStatusResource