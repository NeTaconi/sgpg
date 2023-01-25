from django.forms import ModelForm, CharField, TextInput, DateField, NumberInput, ChoiceField
from .models import Aluno, Graduacao, Endereco, Trabalho, Residencia, Titulacao, Afastamento, EnsinoMedio

class AlunoForm(ModelForm):
    dt_nascimento = DateField(widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'nome_pai', 'nome_mae', 'naturalidade', 'nacionalidade', 'dt_nascimento', 'estado_civil', 'identidade',
                 'identidade_uf', 'identidade_orgao', 'sexo', 'email', 'etnia']

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class GraduacaoForm(ModelForm):
    class Meta:
        model = Graduacao
        fields = '__all__'
        exclude = ['residencia']

class EnsinoMedioForm(ModelForm):
    class Meta:
        model = EnsinoMedio
        fields = '__all__'

class TrabalhoForm(ModelForm):
    data_termino = DateField(widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Trabalho
        fields = '__all__'
        exclude = ['endereco']

class ResidenciaForm(ModelForm):
    class Meta:
        model = Residencia
        fields = '__all__'

class TitulacaoForm(ModelForm):
    data_qualificacao = DateField(widget=NumberInput(attrs={'type':'date'}))
    class Meta:
        model = Titulacao
        fields = '__all__'


class TitulacaoProfessorForm(ModelForm):
    class Meta:
        model = Titulacao
        fields = '__all__'
        exclude = ['data_qualificacao']

class AfastamentoForm(ModelForm):
    class Meta:
        model = Afastamento
        fields = '__all__'