# -*- coding: utf-8 -*- 
from django.db import models
from datetime import date
from companies.models import Funcionario


class Status(models.Model):
	nome = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nome

class Projeto(models.Model):
	nome = models.CharField(max_length=100)
	responsavel = models.ForeignKey(Funcionario)

	def __unicode__(self):
		return self.nome

class Reuniao(models.Model):
	nome = models.CharField(max_length=100)
	date = models.DateField("Data", default=date.today)

	def __unicode__(self):
		return self.nome

class Compromisso(models.Model):
#	nome = models.CharField(max_length=100)
	conteudo = models.TextField("Conteúdo", max_length=1000)
	reuniao = models.ForeignKey(Reuniao)
	projeto = models.ForeignKey(Projeto, blank=True, null=True)
	solicitante = models.ForeignKey(Funcionario)
	responsavel = models.ForeignKey(Funcionario, related_name='funcionario')
	meta_conclusao = models.DateField("Meta para conclusão")	

	def __unicode__(self):
		return u"00%s" % self.id