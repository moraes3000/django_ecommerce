from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

import re

from utils.validacpf import valida_cpf

class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    data_nascimento = models.DateField()
    cpf =  models.CharField(max_length=11,help_text='somente numeros')
    enderece = models.CharField(max_length=255)
    numero = models.CharField(max_length=10, verbose_name='Número')
    bairro = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=2,
        default='SP',
        choices=(
            ('RJ', 'Rio de Janeiro'),
            ('SP', 'São Paulo'),
            ('MG', 'Minas Gerais'),
        )
    )

    def __str__(self):
        return f'{self.usuario}'

    def clean(self):
        error_messages = {}

        if not valida_cpf(self.cpf):
            error_messages['cpf'] ='Digite um cpf Válido'

        if  re.search(r'[^0-9]',self.cep) or len(self.cpf) <=7 :
            error_messages['cep'] = 'Digite um cep Válido'

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:
        verbose_name_plural = "Perfis"
