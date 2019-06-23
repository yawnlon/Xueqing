from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Course(models.Model):

    TYPE_CHOICES = [
        (0, '免费课'),
        (1, '普通课'),
        (2, 'VIP课'),
    ]

    name = models.CharField(
        _('name'),
        max_length=50,
    )

    introduction = models.CharField(
        _('introduction'),
        max_length=1000,
        blank=True,
        default=""
    )

    type = models.IntegerField(
        _('type'),
        choices=TYPE_CHOICES,
        default=0
    )