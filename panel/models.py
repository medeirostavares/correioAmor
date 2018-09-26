from django.db import models
from datetime import datetime
from django.forms import ModelForm
from django.template.defaultfilters import truncatechars

# Create your models here.
class Recado(models.Model):
    STATUS_CHOICES = (
        ('AP', 'Aprovado'),
        ('IN', 'Inativo'),
        ('RP', 'Reprovado'),
    )
    COMENT_PEND = (
        ('S', 'Sim'),
        ('N', 'Não'),
    )
    apelido = models.CharField(default='', max_length=30,verbose_name='Apelido')
    recado = models.TextField(verbose_name='Recado')
    status = models.CharField(default='IN', max_length=2, choices=STATUS_CHOICES, verbose_name='Status')
    publicacao = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Publicação')
    comentario_pendente = models.CharField(editable=False, default='N', max_length=1, choices=COMENT_PEND, verbose_name='Comentário')

    @property
    def resumo(self):
        return truncatechars(self.recado, 50)

    class Meta:
        ordering = ('-publicacao',)
    def __str__(self):
        return self.recado

 #CLASSE PARA INLINE:
class comentariosInline(models.Model):
    STATUS_CHOICES = (
        ('AP', 'Aprovado'),
        ('IN', 'Inativo'),
        ('RP', 'Reprovado'),
    )
    #recado_inline_id --> ForeignKey no BD
    recado_inline = models.ForeignKey(Recado, on_delete=models.CASCADE)
    apelido = models.CharField(default='', max_length=30, verbose_name='Apelido')
    comentario = models.TextField(verbose_name='Comentário')
    status = models.CharField(default='IN', max_length=2, choices=STATUS_CHOICES, verbose_name='Status')
    publicacao = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Publicação')

    @property
    def resumo(self):
        return truncatechars(self.comentario, 50)

    class Meta:
        verbose_name = ('Comentário')
        ordering = ('-publicacao',)

    def __str__(self):
        return self.comentario


class FormRecado(ModelForm):
    class Meta:
        model = Recado
        fields = ('apelido', 'recado',)

class FormComentario(ModelForm):

   #def save(self, recado_edit):
   #     print ('recado_id:', recado_edit)



   class Meta:
        model = comentariosInline
        fields = ('apelido', 'comentario')