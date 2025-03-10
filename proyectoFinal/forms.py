import django.forms as forms

from proyectoFinal.models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.CharField(max_length=200)
    state = forms.ChoiceField(
        choices=[
            ('por_realizar', 'Por Realizar'),
            ('en_transito', 'En Transito'),
            ('completada', 'Completada')
        ]
    )
    class Meta:
        model = Note
        fields = ['title', 'description', 'state']
    # Compare this snippet from proyectoFinal/models.py:
    # from django.db import models
    #
    #
    # class Note(models

