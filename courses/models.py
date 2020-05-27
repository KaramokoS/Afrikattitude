from django.db import models
import random
import os
from django.urls import reverse
from django.contrib.auth.models import User

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField

from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

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
    owner           = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    subject         = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title           = models.CharField(max_length=50)
    image           = models.ImageField(upload_to=upload_image_path, blank=True)
    description     = models.CharField(max_length=500)
    pub_date        = models.DateTimeField(auto_now=True)
    slug            = models.SlugField(max_length=200, unique=True)
    overview        = models.TextField(null=True, blank=True)
    created         = models.DateTimeField(auto_now_add=True)
    students        = models.ManyToManyField(User, related_name='course_joined', blank=True)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id, self.slug])



class Module(models.Model):
    course      = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    order       = OrderField(blank=True, for_fields=['course'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)

class Content(models.Model):
    """docstring for Content."""
    module          = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type    = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                limit_choices_to={'model__in':(
                                    'text',
                                    'video',
                                    'image',
                                    'file')})
    object_id       = models.PositiveIntegerField()
    item            = GenericForeignKey('content_type', 'object_id')
    order           = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner       = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title       = models.CharField(max_length=250)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
                        self._meta.model_name), {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
