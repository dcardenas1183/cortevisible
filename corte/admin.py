from django.contrib import admin
from corte.models import Sentencia
from corte.models import TipoCaso
from corte.models import TipoDemanda

class SentenciaAdmin (admin.ModelAdmin):
    ordering = ('anio',)
    list_display = ('__unicode__', 'anio', 'cod_sentencia', 'proyecto',
            'num_sentencia', 'tipo_caso', 'tipo_demanda', 'id_norma',
            'numero_senado', 'numero_camara')
    list_filter = ('anio', 'tipo_caso', 'tipo_demanda', 'oficio', 'mas_normas')
    search_fields = ['cod_sentencia', 'proyecto', 'id_norma']
    actions_on_bottom = True
    actions_on_top = False

admin.site.register(Sentencia, SentenciaAdmin)
admin.site.register(TipoCaso)
admin.site.register(TipoDemanda)

