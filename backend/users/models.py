from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class SmsCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(_("短信验证码"), max_length = 10)
    mobile = models.CharField(
        _("手机号"), 
        max_length = 11,
        unique=True,
        error_messages={
            'unique': _("A user with that mobile number already exists."),
        })
    add_time = models.DateTimeField(_("添加时间"), auto_now_add=True)

    used = models.BooleanField(_("是否使用过"), default=False)

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
        (0, 'student'),
        (1, 'admin'),
        (2, 'school'),
        (3, 'agent')
    ]

    mobile = models.CharField(
        _('mobile'),
        max_length=11,# 只支持国内的11位手机号
        unique=True,
        error_messages={
            'unique': _("该手机号已经存在"),
        },
        db_index = True
    )

    type = models.IntegerField(
        _('user_type'),
        choices=TYPE_CHOICES,
        default=0
    )

GENDER_CHOICES = [
    (0, "未知"),
    (1, "男"),
    (2, "女")
]

class StudentInfo(models.Model):

    name = models.CharField(
        _('name'),
        max_length=50,
    )

    # head = models.CharField(
    #     _('head_image_url'),
    #     max_length = 500
    # )

    gender = models.IntegerField(
        _('gender'),
        choices=GENDER_CHOICES,
        default=0
    )

    user = models.OneToOneField('BaseInfo', 
        on_delete=models.CASCADE,
        db_index=True)
