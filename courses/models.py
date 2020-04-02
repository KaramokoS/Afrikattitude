from django.db import models
import random
import os
from django.urls import reverse
# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Subject'


    def __str__(self):
        return self.title

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "courses/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename
            )

class Course(models.Model):
    subject = models.ForeignKey(Subject, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=upload_image_path, blank=True)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])
