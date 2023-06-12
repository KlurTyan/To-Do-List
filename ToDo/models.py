from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin
)

from .managers import UserManager

# The to-do table model

class User(AbstractBaseUser, PermissionsMixin):
    SUPERADMIN, CLIENT=range(1,3)

    ROLE_TYPES=(
        (SUPERADMIN,'Суперпользователь'),
        (CLIENT,'Пользователь')
    )

    objects = UserManager()

    id = models.AutoField(primary_key=True)
    username = models.CharField('Логин', max_length=50, default='', unique=True)
    first_name = models.CharField("ФИО",max_length=100, default='', blank=True,null=True)
    email=models.EmailField("Почта",default="email@mail.com",blank=True,null=True)
    role=models.IntegerField(verbose_name='Роль',default=CLIENT,choices=ROLE_TYPES)
    date_joined=models.DateTimeField("Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        verbose_name='Статус доступа',
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Affairs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Пользователь создавший пост"), on_delete=models.CASCADE,null=True,blank=True, related_name='affair')
    text = models.TextField('Дело', max_length=30)
    date = models.DateField('Дата')
    done = models.BooleanField('Выполнено')

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


