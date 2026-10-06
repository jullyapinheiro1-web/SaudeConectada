
from django.contrib import admin
from .models import Vacina, LocalVacinacao, Campanha


admin.site.register(Vacina)
admin.site.register(LocalVacinacao)
admin.site.register(Campanha)