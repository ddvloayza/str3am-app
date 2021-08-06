from django.contrib import admin
from singlemodeladmin import SingleModelAdmin
from apps.web.models import ( Programa, Capitulos, Productora, Principal )

@admin.register(Principal)
class PrincipalAdmin(admin.ModelAdmin):
    list_display = ['order_video', 'nombre_video_principal', 'videos_activo']


@admin.register(Productora)
class ProductoraAdmin(admin.ModelAdmin):
    pass


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ['orden_programa', 'nombre', 'active']


@admin.register(Capitulos)
class CapitulosAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("titulo",)}
	search_fields = ['programa', 'numero_capitulo']
	list_display = ['numero_capitulo', 'programa', 'titulo', 'fecha_emision']
	list_filter = ('programa', 'fecha_emision')
	ordering = ('numero_capitulo',)



