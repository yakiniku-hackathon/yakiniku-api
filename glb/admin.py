from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin

from .models import Model, Vps


class VpsResource(resources.ModelResource):
    class Meta:
        model = Vps

class ModelResource(resources.ModelResource):
    class Meta:
        model = Model


@admin.register(Vps)
class VpsAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = VpsResource

@admin.register(Model)
class QuestionAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = ModelResource