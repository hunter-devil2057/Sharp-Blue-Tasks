from django.db import models

# Create your models here.
class MergedDataSet(models.Model):
    name = models.CharField(max_length = 60)
    row_count = models.PositiveIntegerField(default = 0)
    colm_count = models.PositiveIntegerField(default = 0)
    uploaded_at = models.DateField(auto_now_add=True)
    source_file_count = models.PositiveIntegerField(default = 0)
    merged_file = models.FileField(upload_to = 'merged/')

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name or f"Merged Dataset: #{self.pk}"
    