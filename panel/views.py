from django.shortcuts import render, get_object_or_404
from .models import Recado, comentariosInline
from .forms import FormRecado, FormComentario
from .models import FormRecado, FormComentario
from django import forms


def index(request):
    return render(request, 'index.html', )

def lista_recados(request):
    recado = Recado.objects.all().order_by('-publicacao')
    comentarios = comentariosInline.objects.all().order_by('-publicacao')
    msg_env = ''
    if request.method == 'POST':
        formR = FormRecado(request.POST)
        if formR.is_valid():
            formR.save()
            msg_env = 'Obrigado por contribuir. Seu recado será analizado antes de ser postado...'
            formR = FormRecado()
    else:
        formR = FormRecado()
    return render(request, 'panel.html', {'msg_enviada_sucesso': msg_env, 'comentarios': comentarios, 'recado': recado, 'formulario_envio': formR, })

def comentarios(request, id):
    recado_edit = get_object_or_404(Recado, pk=id)
    recado_id = id
    msg_env = ''
    if request.method == 'POST':
        formC = FormComentario(request.POST)
        if formC.is_valid():
            #VINCULA A INLINE DO COMENTÁRIO AO RECADO:
            post = formC.save(commit=False)
            post.recado_inline_id = recado_id
            post.save()
            pend = Recado(id=recado_id)
            pend.comentario_pendente = 'S'
            pend.save(update_fields=['comentario_pendente'])
            msg_env = 'Obrigado. Seu comentário será analizado antes de ser postado...'
            formC = FormComentario()
    else:
        formC = FormComentario()
    return render(request, 'comentario.html', {'msg_enviada_sucesso': msg_env, 'recado': recado_edit, 'formulario_envio': formC })


def sobre(request):
    return render(request, 'sobre.html', )

def contato(request):
    return render(request, 'contato.html', )

def galeria(request):
    return render(request, 'galeria.html', )

def staff(request):
    return render(request, 'equipe.html', )

def termo(request):
    return render(request, 'termo_de_uso.html', )






    #def comentario(request, id):
    recado = get_object_or_404(Recado, pk=id)
#    try:
#        selected_choice = question.choice_set.get(pk=request.POST['choice'])
#    except (KeyError, Choice.DoesNotExist):
#        # Redisplay the question voting form.
#        return render(request, 'polls/detail.html', {
#            'question': question,
#            'error_message': "You didn't select a choice.",
#        })
#    else:
#        selected_choice.votes += 1
#        selected_choice.save()
#        # Always return an HttpResponseRedirect after successfully dealing
#        # with POST data. This prevents data from being posted twice if a
#        # user hits the Back button.
#        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))