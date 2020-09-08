from django.contrib import admin
from .models import Laptops
from import_export.admin import ImportExportModelAdmin

@admin.register(Laptops)

class ViewAdmin(ImportExportModelAdmin):
    pass

