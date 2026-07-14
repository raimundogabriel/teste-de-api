from django.contrib import admin
from .models import Aluno , Curso

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    # Quais colunas aparecerão na lista geral
    # list_display = ('RA','nome','nascimeto')
    
    # Adiciona uma barra de pesquisa
    search_fields = ('RA','nome','nascimeto')
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
        # Quais colunas aparecerão na lista geral
    #list_display =  ('nomecurso','codigo','cargaHoraria',"datainicio","datatermino")
    
    # Adiciona uma barra de pesquisa
    search_fields =  ('nomecurso','codigo','cargaHoraria',"datainicio","datatermino")