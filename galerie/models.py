from django.db import models
from django.urls import reverse
import random
import os



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext



def upload_image_path(instance, filename):
    # print(instance)
    #print(filename)
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "galerie/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )


class Galerie(models.Model):
    name            = models.CharField(max_length=255)
    description     = models.CharField(max_length=1500, blank=True, null=True)
    photo           = models.ImageField(upload_to=upload_image_path, blank=True, null=True)
    slug            = models.SlugField(unique=True, null=False)

    objects         = models.Manager()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('galerie:galerie_detail', kwargs={'slug': self.slug})
