from django.db import models

# Create your models here.

class Member(models.Model):
    user_id = models.CharField(max_length=128, unique=True, verbose_name='아이디')  #unique = 고유한 값, / 그럼 pk는? : 그건 그것대로 주고 이것도.
    password = models.CharField(max_length=255, verbose_name='비밀번호')
    name = models.CharField(max_length=128, verbose_name='이름')
    age = models.IntegerField(verbose_name='나이')

    def __str__(self):
        # self.name + ': ' + str(self.age) + '세'
        # '%s: %d세' %(self.name, self.age)
        return f'{self.name}: {self.age}세'

    class Meta:
        verbose_name='회원'
        verbose_name_plural='회원'