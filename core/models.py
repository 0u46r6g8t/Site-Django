from django.db import models

# Create your models here.

class Produtos(models.Model):

    name = models.CharField(max_length=100, verbose_name='Nome', blank=False)
    descrition = models.TextField(verbose_name='Descrição', blank=False)
    photo = models.FileField(upload_to="%Y/%m/%d/")


class Attack(models.Model):

    nameAttack = models.CharField(max_length=100, verbose_name='Ataque', blank=False)
    descritionAttack = models.TextField(verbose_name='Sobre', blank=False)
    featureAttack = models.TextField(verbose_name='Caracteristica', blank=False)

    def Meta(self):
        self.nameAttack = 'Attack'