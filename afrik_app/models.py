from django.db import models
from phone_field import PhoneField
# Create your models here.

class Commentaire(models.Model):
    Nom = models.CharField(max_length=50)
    email = models.EmailField()
    Message = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    Téléphone = PhoneField(blank=True, help_text='Numero de Téléphone')


    class Meta:
        ordering = ['created']


    def __str__(self):
        return 'Comment by {} on {}'.format(self.Nom, self.email)
