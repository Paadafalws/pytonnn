from django.contrib import admin
from API.models import Curso,Aluno,Matricula

# Register your models here.
'a visualziaçao do admin'
class Alunos(admin.ModelAdmin):
        list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
        list_display_links = ('id', 'nome')
        search_fields = ('nome','cpf')
        list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos (admin.ModelAdmin):
       list_display = ('id','codigo_curso','descricao','nivel')
       
admin.site.register(Curso, Cursos,)

class Matriculas (admin.ModelAdmin):
       list_display = ('id','aluno','curso','periodo')
       list_display_links = ('id',)

admin.site.register(Matricula,Matriculas)


        