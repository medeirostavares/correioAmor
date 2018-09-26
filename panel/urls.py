from django.urls import path
from .views import lista_recados, sobre, galeria, contato, comentarios, termo, staff

# REQUEST(VIEW) > URL > VIEW > MODEL > RESPONSE

urlpatterns = [
    path('', lista_recados),
    #path('', index),
    #path('recados/', lista_recados),
    path('comentario/<int:id>', comentarios, name='comentario'),
    path('sobre/', sobre),
    path('contato/', contato),
    path('staff/', staff),
    path('galeria/', galeria),
    path('termo/', termo),

]