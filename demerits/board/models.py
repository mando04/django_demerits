from django.db import models
from djangotoolbox.fields import ListField, EmbeddedModelField, DictField
from .forms import StringListField

class CategoryField(ListField):
    def formfield(self, **kwargs):
        return models.Field.formfield(self, StringListField, **kwargs)

class PersonD(models.Model):
    name = models.CharField(unique=True, max_length=32)
    demerits = DictField()

