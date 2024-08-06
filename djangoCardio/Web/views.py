from django.shortcuts import render
import joblib
import numpy as np
import os
from django.conf import settings
from .forms import PredictionForm

# Ruta absoluta al archivo del modelo
model_path = os.path.join(settings.BASE_DIR, 'random_forest_model_HRA2.pkl')
model = joblib.load(model_path)

def homeView(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            input_data = np.array([[
                data['edad'], data['genero'], data['talla'], data['peso'],
                data['P_sistolica'], data['P_diastolica'], data['colesterol'],
                data['glucosa'], data['fumador'], data['alcohol'], data['actividadFisica']
            ]])
            prediction = model.predict(input_data)
            result = 'Con Cardiopatía al 72 % de probabilidad' if prediction[0] == 1 else 'Sin Cardiopatía al 72% probabilidad'
            return render(request, 'result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'home.html', {'form': form})
