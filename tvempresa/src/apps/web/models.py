from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Principal(models.Model):
	nombre_video_principal = models.CharField('Nombre Video Principal', max_length=200, blank=True, null=True)
	video_principal = models.URLField('Video Principal', blank=True, null=True)
	videos_activo = models.BooleanField('Video Activo', default=True)
	order_video = models.IntegerField('Orden del Videos', blank=True, null=True, unique=True)
	def __str__(self):
		return self.nombre_video_principal
		
	class Meta:
		verbose_name = "Video Principal"
		verbose_name_plural = "Videos Principales"
		ordering = ['order_video']

class Productora(models.Model):
	nombre_productora = models.CharField('Nombre Productora', max_length=200)
	imagen_productora = models.ImageField('Imagen Productora', max_length=200, upload_to='productoras/', help_text="Tamaño 664x362", blank=True, null=True)

	def __str__(self):
		return self.nombre_productora


class Programa(models.Model):
	usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
	nombre = models.CharField('Nombre', max_length=200)
	orden_programa = models.IntegerField('Orden Programa', blank=True, null=True, unique=True)
	imagen_programa = models.ImageField('Imagen Programa', max_length=200, upload_to='programas/', help_text="Tamaño 664x362", blank=True, null=True)
	active = models.BooleanField('Active', default=True)
	productora = models.ForeignKey(Productora, blank=True, null=True, on_delete=models.CASCADE)
	 

	class Meta:
		verbose_name = "Programa"
		verbose_name_plural = "Programas"
		ordering = ['orden_programa']

	def __str__(self):
		return self.nombre

	


class Capitulos(models.Model):
	programa = models.ForeignKey(Programa, related_name='programa', on_delete=models.CASCADE)
	numero_capitulo = models.IntegerField('Numero')
	fecha_emision = models.DateTimeField('Fecha de emision')
	titulo = models.TextField('Titulo', max_length=70, blank=True, null=True)
	descripcion = models.TextField('Descripcion', blank=True, null=True)
	imagen_principal = models.ImageField('Imagen Principal', max_length=200, upload_to='capitulos/', help_text="Tamaño 664x362", blank=True, null=True)
	video = models.URLField('Video url', blank=True, null=True)
	slug = models.SlugField(max_length=2000, blank=True, null=True)
	tags = TaggableManager(blank=True)
	logo_titulo = models.ImageField('Logo Titulo', upload_to='logos_titulos/', blank=True, null=True)
	nombre_productora_por_capitulo = models.CharField('Nombre Productora por Capitulo', max_length=200, blank=True, null=True)
	mostrar_principal = models.BooleanField('Mostrar en principal', default=True)
	

	class Meta:
		verbose_name = "Capitulo"
		verbose_name_plural = "Capitulos"
		ordering = ['-numero_capitulo']

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return reverse('web:capitulo_detalle', kwargs={'slug': self.slug})




		
