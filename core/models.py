from django.db import models

# Create your models hereNmodels.CharField('nome', max_length=100)
preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
estoque = models.IntegerField('Quantidade em estoque')

# Model exemplo didático


class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self) -> str:
        return self.nome


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)

    def __str__(self) -> str:
        return f'{self.nome} {self.sobrenome}'

