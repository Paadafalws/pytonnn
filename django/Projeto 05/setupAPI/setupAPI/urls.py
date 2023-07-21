from django.contrib import admin
from django.urls import include, path
from API.views import AlunosViewSet,CursosViewSet,MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('cursos', MatriculaViewSet, basename='Matricula')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls) )
]