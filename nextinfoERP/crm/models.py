from django.db import models
from django.utils.translation import ugettext_lazy as _

class Pessoa(models.Model):
    first_name = models.CharField(_(u'nome'), max_length=15)
    last_name = models.CharField(_(u'sobrenome'), max_length=15)


class PessoaFisica(Pessoa):
    cpf = models.CharField(_('CPF'), max_length=11,unique=True)
    rg = models.CharField(_('RG'), max_length=11)


class PessoaJuridica(Pessoa):
    cnpj = models.CharField(_('CNPJ'), max_length=11,unique=True)
    ie = models.CharField(_('IE'), max_length=20, default='isento')
