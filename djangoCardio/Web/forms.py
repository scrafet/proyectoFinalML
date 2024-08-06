from django import forms

class PredictionForm(forms.Form):
    edad = forms.IntegerField(
        label='Edad',
    help_text = 'Años'
    )
    genero = forms.ChoiceField(choices=[(1, 'Masculino'), (2, 'Femenino')], label='Género')
    talla = forms.FloatField(
        label='Talla',
    help_text = 'Cm.'
    )
    peso = forms.FloatField(
        label='Peso',
    help_text = 'Kg.',
    )
    P_sistolica = forms.IntegerField(
        label='Presión Sistólica',
        help_text='Valor promedio OMS: 120/91 mmHg (Máx/Min)',
        widget=forms.NumberInput(attrs={'placeholder': '120'})
        )
    P_diastolica = forms.IntegerField(
        label='Presión Diastólica',
    help_text = 'Valor promedio OMS: 80/61 mmHg (Máx/Min)',
    widget = forms.NumberInput(attrs={'placeholder': '80'})
    )

    colesterol = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Por encima de lo normal'), (3, 'Muy por encima de lo normal')], label='Colesterol')
    glucosa = forms.ChoiceField(choices=[(1, 'Normal'), (2, 'Por encima de lo normal'), (3, 'Muy por encima de lo normal')], label='Glucosa')
    fumador = forms.ChoiceField(choices=[(0, 'No'), (1, 'Sí')], label='Fumador')
    alcohol = forms.ChoiceField(choices=[(0, 'No'), (1, 'Sí')], label='Consumo de Alcohol')
    actividadFisica = forms.ChoiceField(choices=[(0, 'No'), (1, 'Sí')], label='Actividad Física')
