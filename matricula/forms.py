from django import forms
from .models import Afastamento, Bolsa, Matricula, Probatorio, Inscricao, TrabalhoFinal

class MatriculaForm(forms.ModelForm):

    class Meta:
        model = Matricula
        fields = ['numero', 'probatorio', 'requisita_bolsa']


class ProbatorioForm(forms.ModelForm):

    class Meta:
        model = Probatorio
        fields = ['data_inscricao', 'nota', 'aluno']

class BolsaForm(forms.ModelForm):

    class Meta:
        model = Bolsa
        fields = ['iniciacao_cientifica', 'nome', 'agencia', 'dt_inicio']

class AfastamentoForm(forms.ModelForm):

    class Meta:
        model = Afastamento
        fields = ['motivo', 'saida', 'retorno']


class InscricaoForm(forms.ModelForm):

    class Meta:
        model = Inscricao
        fields = ['disciplina_ofertada', 'nota']


class TrabalhoFinalForm(forms.ModelForm):

    class Meta:
        model = TrabalhoFinal
        fields = ['titulo', 'data', 'resumo', 'resultado', 'diploma', 'dt_diploma', 'versao_final', 'dt_versao']