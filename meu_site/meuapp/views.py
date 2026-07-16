import logging
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Aluno,Curso

logger = logging.getLogger(__name__)


# Create your views here.
def ola_mundo(request):
    return HttpResponse("<h1>olaaaaaaaaaaa</h1>" \
    "<br><br><br>" \
    "console.log('teste123')"
    "<h2>mundo</h2>")

def lista_alunos(request):
    dados={
        'ra':'11111',
        'nome':'Gabriel',
        'nascimento':'1997-07-08'
    }
    return JsonResponse(dados)


class AlunoView(View):
    def get(self, request):
        # Renderiza a tela com a lista de aluno
        aluno = Aluno.objects.all()
        return render(request, 'aluno/cadastro.html', {'aluno': aluno})

    def post(self, request):
        # Captura e salva os dados
        aluno = Aluno.objects.all()
        # logger.info(aluno)
        ra = request.POST.get('ra')
        nome = request.POST.get('nome')
        nascimento = request.POST.get('nascimento')
        logger.info(f"Aluno criado com os dados {ra} | {nome} | {nascimento}")
        if ra and nome and nascimento:
            Aluno.objects.create(ra=ra,nome=nome,nascimento=nascimento)
            
        return render(request, 'aluno/cadastro.html', {'aluno': aluno})



class CursoView(View):
    def get(self,request):
        curso = Curso.objects.all()
        return render(request, 'aluno/cadastro_curso.html', {'curso': curso})


    def post(self,request):
        curso = Curso.objects.all()
        codigo = request.POST.get('codigo')
        nomecurso = request.POST.get('nomecurso')
        cargarHoraria = request.POST.get('cargarHoraria')
        datainicio = request.POST.get('datainicio')
        dataTermino = request.POST.get('dataTermino')

        logger.info(
            f"Curso criado: {codigo} | {nomecurso} | {cargarHoraria} | {datainicio} | {dataTermino}")
        

        if (codigo and nomecurso and cargarHoraria and datainicio and dataTermino):
            Curso.objects.create(codigo=codigo,nomecurso=nomecurso,cargarHoraria=cargarHoraria,datainicio=datainicio,dataTermino=dataTermino)

        return render(request, 'aluno/cadastro_curso.html' , {'curso': curso})