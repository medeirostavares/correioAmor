from django import forms
from panel.models import Recado, comentariosInline

class FormRecado(forms.Form):
    nome = forms.CharField(label='Apelido', max_length=10)
    # email = forms.EmailField(required=False)
    recado = forms.Field(widget=forms.Textarea)

    class Meta:
        model = Recado
        #fields = ('nome', 'recado',)

class FormComentario(forms.Form):
    nome = forms.CharField(label='Apelido', max_length=10)
    # email = forms.EmailField(required=False)
    comentario = forms.Field(widget=forms.Textarea)

    class Meta:
        model = comentariosInline
        #fields = ('nome', 'recado',)

#form_com = FormRecado(
#    {'nome': 'john', 'recado': 'john@example.com'})
#if form_com.is_valid():
#    form_com.save()