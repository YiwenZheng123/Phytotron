from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '账号管理'
        verbose_name = '账号管理'
        app_label = 'users'
