from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'topic', 'inventory_number', 'cell_code', 'quantity', 'arrival_date']
        labels = {
            'title': 'Название',
            'topic': 'Тема',
            'inventory_number': 'Инвентарный номер',
            'cell_code': 'Код ячейки',
            'quantity': 'Количество',
            'arrival_date': 'Дата поступления',
        }
