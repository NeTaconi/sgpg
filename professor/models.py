from django.db import models
from aluno.models import Endereco, Titulacao, Graduacao
from django.contrib.auth.models import User
# Create your models here.

class PosDoutorado(models.Model):
      concluido = models.BooleanField()
      ano_inicio = models.IntegerField(null=True, blank=True)
      ano_fim = models.IntegerField(null=True, blank=True)
      instituicao_posdoc = models.CharField(max_length=200, null=True, blank=True)
      pais = models.CharField(max_length=200, null=True, blank=True)

class Trabalho(models.Model):
      instituicao_trabalho = models.CharField(max_length=200)
      setor = models.CharField(max_length=200, null=True, blank=True)
      admissao = models .DateField(null=True, blank=True)
      cargo = models.CharField(max_length=200)
      telefone  = models.CharField(max_length=15, null=True, blank=True)
      categoria = models.CharField(max_length=200, null=True, blank=True) 
      email = models.EmailField(null=True, blank=True)

      def __str__(self):
            return self.instituicao


class Professor(models.Model):

      TIPO_DOCENTE_CHOICES = (
            ("Permanente", "Permanente"),
            ("Colaborador", "Colaborador"),
            ("Coorientador", "Coorientador"),
            ("Visitante", "Visitante"),
            ("Pos Doutor", "Pós Doutor"),
      )

      nome = models.CharField(max_length=200)
      sexo = models.CharField(max_length=50, null=True, blank=True)
      dt_nascimento = models.DateField(null=True, blank=True)
      nacionalidade = models.CharField(max_length=100, null=True, blank=True)
      naturalidade = models.CharField(max_length=2, null=True, blank=True)
      cpf = models.CharField(max_length=14, null=True, blank=True)
      identidade = models.CharField(max_length=12, null=True, blank=True)
      identidade_uf= models.CharField(max_length=2, null=True, blank=True)
      identidade_orgao = models.CharField(max_length=100, null=True, blank=True)
      tipo_docente = models.CharField(max_length=100, choices=TIPO_DOCENTE_CHOICES, null=True, blank=True)
      endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
      titulacao = models.OneToOneField(Titulacao, on_delete=models.DO_NOTHING)
      graduacao = models.OneToOneField(Graduacao, on_delete=models.DO_NOTHING, null=True)
      trabalho = models.ForeignKey(Trabalho, on_delete=models.DO_NOTHING, related_name="professor_trabalho")
      pos_doutorado = models.ForeignKey(PosDoutorado, on_delete=models.DO_NOTHING, related_name="professor_pos_doutorado")

      slug = models.SlugField(max_length=250, unique_for_date='dt_cadastro')
      updated = models.DateTimeField(auto_now=True)
      cadastrado_por = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='professor_cadastrado_por')

      def __str__(self):
            return  self.nome