from django.contrib import admin
from django.urls import path,include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet, basename='Alunos')
router.register(r'cursos', CursosViewSet, basename='Cursos',)
router.register(r'matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path(r'cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
