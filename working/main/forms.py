from django import forms

class ExcelForm(forms.Form):
    name = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)
        self.fields['name'].choices = choices
        
        
class UploadExcelForm(forms.Form):
    excel_file = forms.FileField()
