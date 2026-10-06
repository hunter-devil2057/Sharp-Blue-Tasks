from django.contrib import admin
from .models import MergedDataSet

# Register your models here.
@admin.register(MergedDataSet)
class MergedDatasetAdmin(admin.ModelAdmin):
    list_display = ('name', 'row_count', 'colm_count', 'uploaded_at')