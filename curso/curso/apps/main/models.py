from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	usuario = models.OneToOneField(User)
	telefono = models.CharField(max_length=20)
	dereccion = models.TextField()
	
	def __unicode__(self):
		return self.usuario.username
	
	class Meta:
		verbose_name_plural = ('Perfiles')
