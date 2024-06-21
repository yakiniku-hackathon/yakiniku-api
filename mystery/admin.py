from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin

from .models import Mystery, Question


class MysteryResource(resources.ModelResource):
    class Meta:
        model = Mystery

class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question


@admin.register(Mystery)
class MysteryAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = MysteryResource

@admin.register(Question)
class QuestionAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = QuestionResource