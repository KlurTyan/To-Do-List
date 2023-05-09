from django.db import models

# The to-do table model

class Affairs(models.Model):
    text = models.TextField('Дело', max_length=30)
    date = models.DateField('Дата')
    done = models.BooleanField('Выполнено')

    def __str__(self) -> str:
        return self.text
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


