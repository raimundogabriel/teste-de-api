from django.db import models

# Create your models here.
class Aluno(models.Model):
    RA =  models.IntegerField(verbose_name="Digite sua RA",primary_key=True)
    nome = models.CharField(max_length=50,verbose_name="Nome completo")
    nascimento = models.DateField(verbose_name="Digite sua idade")


    def __str__(self):
        return f"{self.nome}  ({self.RA})  {self.nascimento}"
    class Meta:
        verbose_name ="Aluno"
        verbose_name_plural = "Alunos"
class Curso(models.Model):
    codigo = models.IntegerField(verbose_name="Digite o codigo!", primary_key=True)
    nomecurso =  models.CharField(max_length=100,verbose_name="Digite o nome do curso")
    cargarHoraria = models.IntegerField(verbose_name='Digite a carga horária do curso')
    datainicio =  models.DateField(verbose_name='Digite ínicio')
    dataTermino=   models.DateField(verbose_name='Digite Término')     

    def __str__(self):
        return f'({self.codigo}) {self.nomecurso} {self.cargarHoraria} {self.datainicio} {self.dataTermino}'