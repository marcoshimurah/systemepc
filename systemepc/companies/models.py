from django.db import models

class Cargo(models.Model):
	nome = models.CharField(max_length=100, unique = True)

	def __unicode__(self):
		return self.nome

class Lotacao(models.Model):
	nome = models.CharField(max_length=100, unique = True)
	sigla = models.CharField(max_length=20)
	
	def __unicode__(self):
		return self.nome

class Vinculo(models.Model):
	nome = models.CharField(max_length=100, unique = True)

	def __unicode__(self):
		return self.nome

class Situacao(models.Model):
	nome = models.CharField(max_length=50, unique = True)

	def __unicode__(self):
		return self.nome

class Funcionario(models.Model):
	nome = models.CharField(max_length=100, unique = True)
	matricula = models.IntegerField(unique=True)
	email = models.EmailField(max_length=100, unique=True)
	cargo = models.ForeignKey(Cargo)
	lotacao = models.ForeignKey(Lotacao)
	chefia_imediata = models.ForeignKey('self', blank=True, null=True, related_name='chefia imediata')
	vinculo = models.ForeignKey(Vinculo)
	situacao = models.ForeignKey(Situacao)
	
	def __unicode__(self):
		return self.nome
