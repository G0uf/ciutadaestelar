# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Fabricant(models.Model):
    #insertar mes coses
    nom = models.CharField(unique=True, verbose_name="Nom", max_length=20, help_text="El nom del fabricant del producte.")
    logo = models.ImageField(verbose_name="Logo", upload_to="Logo", height_field=None, width_field=None, help_text="Logo del fabricant")
    especialitzacio = models.TextField(verbose_name="Especialització", max_length=800, help_text="Descripcio del fabricant i quina es la especialitzacio de la empresa")
    
    def __unicode__(self):
        return u'%s' % (self.nom)
        
class Arma(models.Model):
    nom = models.CharField(unique=True, verbose_name="Nom", max_length=30, help_text="Nom del model de l'arma")
    imatge = models.ImageField(verbose_name="Imatge", upload_to="Arma", height_field=None, width_field=None, help_text="Imatge de l'arma")
    silueta = models.ImageField(verbose_name="Silueta", upload_to="Arma", height_field=None, width_field=None, help_text="Silueta de l'arma")
    descripcio = models.TextField(verbose_name="Descripció", max_length=1300, help_text="Petita descripcio de l'arma")
    #dades de la arma
    dany = models.IntegerField(verbose_name="Dany", help_text="Dany que fa cada impacte")
    velocitat = models.IntegerField(verbose_name="Velocitat", help_text="Velocitat a la que va el projectil")
    calormax = models.IntegerField(verbose_name="CalorMaxim", help_text="Limit de calor que te l'arma fins que deixa de disparar")
    calorgen = models.IntegerField(verbose_name="CalorGenerat", help_text="Calor que genera l'arma per cada tir")
    #preu
    preucredits = models.IntegerField(verbose_name="PreuCredits", help_text="El preu de la nau en credits del joc")
    
    def __unicode__(self):
        return u'%s' % (self.nom)
    
class Misil(models.Model):
    nom = models.CharField(unique=True, verbose_name="Nom", max_length=30, help_text="Nom del model del misil")
    imatge = models.ImageField(verbose_name="Imatge", upload_to="Misil", height_field=None, width_field=None, help_text="Imatge del misil")
    silueta = models.ImageField(verbose_name="Silueta", upload_to="Misil", height_field=None, width_field=None, help_text="Silueta del misil")
    descripcio = models.TextField(verbose_name="Descripció", max_length=800, help_text="Petita descripcio del misil")
    #dades de la arma
    dany = models.IntegerField(verbose_name="Dany", help_text="Dany que fa cada imapacte")
    velocitat = models.IntegerField(verbose_name="Velocitat", help_text="Velocitat a la que va el misil")
    salut = models.IntegerField(verbose_name="salut", help_text="Vida que te el misil avans de explotar")
    guiat = models.BooleanField(default=False, verbose_name="Guiat", help_text="El misil segueix a el enemic o no")
    #preu
    preucredits = models.IntegerField(verbose_name="PreuCredits", help_text="El preu de la nau en credits del joc")
    
    def __unicode__(self):
        return u'%s' % (self.nom)
    
class Nau(models.Model):
    nom = models.CharField(unique=True, verbose_name="Nom", max_length=30, help_text="Nom del model de la nau")
    imatge = models.ImageField(verbose_name="Imatge", upload_to="Nau", height_field=None, width_field=None, help_text="Imatge de la nau")
    silueta = models.ImageField(verbose_name="Silueta", upload_to="Nau", height_field=None, width_field=None, help_text="Silueta de la nau")
    descripcio = models.TextField(verbose_name="Descripció", max_length=800, help_text="Petita descripcio de la nau")
    fabricant = models.ForeignKey(Fabricant, verbose_name="Fabricant", help_text="Fabricant de la nau")
    video = models.CharField(verbose_name="Demostració", max_length=150, null=True, blank=True, help_text="La demostració mitjançant una URL d'un vídeo.")
    #dades de la nau
    salut = models.IntegerField(verbose_name="salut", help_text="Punts de salut que te la nau")
    escuts = models.IntegerField(verbose_name="Escuts", help_text="Punts de escut que te la nau")
    velocitat = models.IntegerField(verbose_name="Velocitat", help_text="Velocitat a la que es desplaça la nau")
    disipaciocal = models.IntegerField(verbose_name="DisipacióCalor", help_text="Quantitat de calor que disipa")
    numarmes = models.IntegerField(verbose_name="NumeroArmes", help_text="Quantitat de armes que porta la nau")
    armes = models.ManyToManyField(Arma, verbose_name="Armes", help_text="Les armes que porta equipada la nau")
    nummisils = models.IntegerField(verbose_name="NumeroMisils", help_text="Quantitat de misils que porta la nau")
    misil = models.ForeignKey(Misil, verbose_name="Misil", help_text="El tipus de misil que porta equipada la nau")
    #preu
    preucredits = models.IntegerField(verbose_name="PreuCredits", help_text="El preu de la nau en credits del joc")
    preu = models.DecimalField(verbose_name="Preu", max_digits=5, decimal_places=2, help_text="El preu del producte en diners.")
    
    class Meta:
        unique_together = [('nom', 'fabricant')]
    
    def __unicode__(self):
        return u'%s' % (self.nom)