from django.contrib import admin
from .models import Recado, comentariosInline
from django.db.models import Count

# Register your models here.

def ativar_recado(modeladmin, request, queryset):
    queryset.update(status='AP')

class AdminComentariosInline(admin.StackedInline):
    model = comentariosInline
    readonly_fields = ('apelido', 'comentario', 'publicacao')
    fk_name = 'recado_inline'
    extra = 0;
    fields = ['recado_inline', 'apelido', 'status', 'publicacao']
    ordering = ('-publicacao', '-apelido',)
    search_fields = ('apelido', 'comentario', 'publicacao')

    def has_add_permission(self, request, obj=model):
        return False

class AdminRecado(admin.ModelAdmin):
    model = Recado

    def get_queryset(self, request):
        qs = super(AdminRecado, self).get_queryset(request)
        return qs.annotate(conta_comentarios=Count('menu_items'))

    def conta_comentarios(self, inst):
        return inst.conta_comentarios

    list_display = ('status', 'apelido', 'resumo', 'publicacao', 'comentario_pendente', 'conta_comentarios')

    inlines = [AdminComentariosInline, ]

    list_filter = ('publicacao',)
    readonly_fields = ['apelido', 'recado', 'publicacao']
    ordering = ('-publicacao','-apelido',)
    search_fields = ('apelido', 'recado', 'publicacao')
    actions = [ativar_recado]

    def has_add_permission(self, request, obj=model):
        return False



admin.site.site_header = "Administração - Correio do Amor"
admin.site.index_title = "Correio do Amor"
admin.site.site_title = "Painel"

ativar_recado.short_description = "Marcar selecionados como Aprovado"
admin.site.register(Recado, AdminRecado)

#admin.site.disable_action('delete_selected')

