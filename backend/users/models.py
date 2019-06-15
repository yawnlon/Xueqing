from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class SmsCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(_("短信验证码"), max_length = 10)
    mobile = models.CharField(_("手机号"), max_length = 11)
    add_time = models.DateTimeField(_("添加时间"), default = datetime.now)

    class Meta:
        verbose_name = _("短信验证")
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

# Create your models here.
class BaseInfo(AbstractUser):
    """
    用户信息
    """

    TYPE_CHOICES = [
        (0, 'normal'),
        (1, 'admin'),
        (2, 'school'),
        (3, 'agent')
    ]

    mobile = models.CharField(
        _('mobile'),
        max_length=11,# 只支持国内的11位手机号
        unique=True,
        error_messages={
            'unique': _("A user with that mobile number already exists."),
        }
    )

    type = models.IntegerField(
        _('user_type'),
        choices=TYPE_CHOICES,
        default=0
    )
