from django.contrib import admin

# Register your models here.
from .models import Medicamento, Medico, Utente, Receita
admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Utente)
admin.site.register(Receita)