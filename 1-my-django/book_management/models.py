from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class Book(models.Model):
  name = models.CharField(max_length=100)
  author = models.TextField(blank=False, null=False)
  description = models.TextField(blank=True, null=True)
  image = models.FileField(upload_to='images/', blank=True, null=True)

  def _str_(self):
    return self.name

  def image_tag(self):
        if self.image:
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.image.url))  # Get Image url

  image_tag.short_description = 'Image'