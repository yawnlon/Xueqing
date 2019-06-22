from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class StudyCard(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
    )

    code = models.CharField(
        _('code'),
        max_length=50,
        unique=True
    )

    introduction = models.CharField(
        _('introduction'),
        max_length=1000,
        blank=True,
        default=""
    )

    class_free = models.BooleanField(
        _('class_free'),
        default=False
    )

    class_general = models.BooleanField(
        _('class_general'),
        default=False
    )

    class_vip = models.BooleanField(
        _('class_vip'),
        default=False
    )

    add_time = models.DateTimeField(
        _("add_time"), 
        auto_now_add=True
    )

    



