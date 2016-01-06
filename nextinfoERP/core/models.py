from django.db import models
from django.db.models import Sum, F
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format

ativo_lista = [('A', 'Ativo'), ('I', 'Inativo')]
tipo_pessoa = [('F', 'Fisica'), ('J', 'Juridica')]


class TimeStampedModel(models.Model):
    data_criacao = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    data_modificacao = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True

class Ativo(TimeStampedModel):
    ativo = models.CharField(_(u'ativo'), max_length=15, choices= ativo_lista)
    class Meta:
        abstract = True


class Pessoa(Ativo):
    tipo_pessoa = models.CharField(_(u'tipo'), max_length=15, choices= tipo_pessoa)
    class Meta:
        ordering = ['ativo','tipo_pessoa']

class PessoaFisica(models.Model):
    pessoa = models.ForeignKey('Pessoa',  verbose_name=_('pessoa'))
    nomeCompleto = models.CharField(_('Nome'), max_length=40)
    cpf = models.CharField(_('CPF'), max_length=11,unique=True)
    rg = models.CharField(_('RG'), max_length=11)
    class Meta:
        ordering = ['pessoa','nomeCompleto','cpf']

class PessoaJuridica(models.Model):
    cnpj = models.CharField(_('Cnpj'), max_length=11,unique=True)
    site = models.CharField(_('Site'), max_length=20)
    nomeFantasia = models.CharField(_('NomeFantasia'), max_length=20)
    razaoSocial = models.CharField(_('RazaoSocial'), max_length=20)
    pessoa = models.ForeignKey('Pessoa', verbose_name=_('pessoa'))

    class Meta:
        ordering = ['cnpj','nomeFantasia']
