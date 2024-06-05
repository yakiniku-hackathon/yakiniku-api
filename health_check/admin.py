from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin, ImportExportModelAdmin

from .models import HealthCheck


class HealthCheckResource(resources.ModelResource):
    class Meta:
        model = HealthCheck


@admin.register(HealthCheck)
class HealthCheckAdmin(ImportExportModelAdmin, ExportMixin):
    ordering = ['id']

    resource_class = HealthCheckResource