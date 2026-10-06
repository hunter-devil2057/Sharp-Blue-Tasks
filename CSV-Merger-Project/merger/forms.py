# Importing Form from Django
from django import forms

# Allowing Multiple Files
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

# Enabling Multiple File Fields
class MultipleFileField(forms.FileField):
    # Filefiled accepting multiple files
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_file_clean(d, initial) for d in data]
        return single_file_clean(data, initial)

class CSVUploadForm(forms.Form):
    csv_files = MultipleFileField(
        label = "Select one or more CSV File", 
        help_text = "You can select multiple files at once. Only .csv Files are Processed..."
    )