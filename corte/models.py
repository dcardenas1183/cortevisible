# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from django.utils.translation import ugettext_lazy as _

#from cvisible.proyecto_de_ley.models import ProyectoLey


class Sentencia(models.Model):
   # proyecto = models.ForeignKey(ProyectoLey, blank=True, null=True)
    proyecto = models.CharField(max_length=25, verbose_name=_(u'Proyecto_id'),
            blank=True, null=True)
    anio = models.CharField(max_length=4, verbose_name=_(u'Año'))
    cod_sentencia = models.CharField(
        max_length=20,
        verbose_name=_(u'Código de la sentencia'),
        help_text=_(
            u'Número de sentencia (Cxxx); se puede incluir al final una letra '
            u'(ej. SENTENCIA CxxxA) en caso de que sea necesario'),
    )
    num_sentencia = models.CharField(max_length=20,
                                     verbose_name=_(u'Número de la sentencia'),
                                     help_text=_(u'Número de sentencia sin caracteres'))
    tipo_caso = models.ForeignKey('TipoCaso',
                                  help_text=_(u'Tipo de caso en discusión'))
    id_norma = models.TextField(
        verbose_name=_(u'Número de identificación de la norma demandada'))
    titulo_norma = models.TextField(
        verbose_name=_(u'Título de la norma demandada'))
    mas_normas = models.BooleanField(
        verbose_name=_(u'¿Hay otras normas demandadas?'))
    otras_normas = models.TextField(
        verbose_name=_(u'Normas demandadas adicionales'),
        help_text=_(
            u'Incluir como texto cuáles son las normas demandadas adicionales,'
            u' separadas por punto y coma (ej. ‘Ley xxx de 1993; Ley www de'
            u' 1987’); 9999 si no hay otras normas.')
    )
    numero_camara = models.CharField(max_length=100, help_text='ej. 149/01 (9999 si no aplica).')
    numero_senado = models.CharField(max_length=100, help_text='ej. 197/03 (9999 si no aplica).')
    tipo_demanda = models.ForeignKey('TipoDemanda')
    oficio = models.BooleanField(
        verbose_name=_(u'¿Es revisión de oficio?'))
    fecha_norma = models.DateField(
        verbose_name=_(u'Fecha expedición de la norma demandada'))

    def __unicode__(self):
        return u"%s-%s" % (self.anio, self.cod_sentencia)


class TipoCaso(models.Model):
    descripcion = models.CharField(max_length=150)

    def __unicode__(self):
        return u"%s" % (self.descripcion)


class TipoDemanda(models.Model):
    descripcion = models.CharField(max_length=150)

    def __unicode__(self):
        return u"%s" % (self.descripcion)
